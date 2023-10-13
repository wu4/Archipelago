import settings

class MetroidPrimeSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Metroid Prime v1.00 ISO"""
        description = "Metroid Prime v1.00 ISO File"
        copy_to = "Metroid Prime 1.00.iso"
        md5s = [
            "eeacd0ced8e2bae491eca14f141a4b7c",  # officially shown on randomprime github
        ]

    class RomStart(str):
        """
        Set this to false to never autostart a rom (such as after patching),
                    true  for operating system default program
        Alternatively, a path to a program to open the .iso file with
        """

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: RomStart | bool = True