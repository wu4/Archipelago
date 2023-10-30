from __future__ import annotations

import platform

import dolphin_memory_engine as dolphin
import pid

from .memory_operation import (
    MemoryOperation,
    MemoryOperationException,
    MemoryOperationExecutor,
)

MEM1_START = 0x80000000
MEM1_END = 0x81800000


def _validate_range(address: int, size: int):
    if address < MEM1_START or address + size > MEM1_END:
        raise MemoryOperationException(
            f"Range {address:x} -> {address + size:x} is outside of the GameCube memory range."
        )


class DolphinExecutor(MemoryOperationExecutor):
    def __init__(self):
        super().__init__()
        self._pid = pid.PidFile("mprime-client-dolphin-backend")

    @property
    def lock_identifier(self) -> str | None:
        return "mprime-client-dolphin-backend"

    async def connect(self) -> str | None:
        if platform.system() == "Darwin":
            return "macOS is not supported"

        if not dolphin.is_hooked():
            dolphin.hook()

        if not dolphin.is_hooked():
            return "Unable to connect to Dolphin"

        try:
            self._pid.create()
        except pid.PidFileError:
            return "Another client is connected to Dolphin already"

        return None

    def disconnect(self):
        self._pid.close()
        dolphin.un_hook()

    def _test_still_hooked(self):
        try:
            if len(dolphin.read_bytes(0x0, 4)) != 4:
                raise RuntimeError("Dolphin hook didn't read the correct byte count")
        except RuntimeError as e:
            self.logger.warning(f"Test read for Dolphin hook didn't work: {e}")
            dolphin.un_hook()

    def is_connected(self) -> bool:
        if dolphin.is_hooked():
            self._test_still_hooked()

        return dolphin.is_hooked()

    # Game Backend Stuff
    def _memory_operation(self, op: MemoryOperation, pointers: dict[int, int | None]) -> bytes | None:
        op.validate_byte_sizes()

        address = op.address
        if op.offset is not None:
            if address not in pointers:
                raise MemoryOperationException(f"Invalid op: {address:x} is not in pointers")

            new_address = pointers[address]
            if new_address is None:
                return None
            address = new_address + op.offset

        _validate_range(address, op.byte_count)

        if not dolphin.is_hooked():
            raise MemoryOperationException("Lost connection to Dolphin")

        try:
            result = None
            if op.read_byte_count is not None:
                result = dolphin.read_bytes(address, op.read_byte_count)

            if op.write_bytes is not None:
                dolphin.write_bytes(address, op.write_bytes)
                self.logger.debug(f"Wrote {op.write_bytes.hex()} to {address:x}")

        except RuntimeError as e:
            raise MemoryOperationException(f"Lost connection to Dolphin: {e}")

        return result

    async def perform_memory_operations(self, ops: list[MemoryOperation]) -> dict[MemoryOperation, bytes]:
        pointers_to_read = set()
        for op in ops:
            if op.offset is not None:
                pointers_to_read.add(op.address)

        pointers = {}
        for pointer in pointers_to_read:
            if not dolphin.is_hooked():
                raise MemoryOperationException("Lost connection to Dolphin")

            try:
                pointers[pointer] = dolphin.follow_pointers(pointer, [0])
            except RuntimeError:
                pointers[pointer] = None
                self.logger.debug(f"Failed to read a valid pointer from {pointer:x}")
                self._test_still_hooked()

            if not dolphin.is_hooked():
                raise MemoryOperationException("Lost connection to Dolphin")

        result = {}
        for op in ops:
            op_result = self._memory_operation(op, pointers)
            if op_result is not None:
                result[op] = op_result
        return result
