def relative_to_file(file_path: str, rel_path: str) -> str:
    import os.path
    return os.path.join(os.path.dirname(os.path.abspath(file_path)), rel_path)

def intersperse(val, sequence):
    first = True
    for item in sequence:
        if not first:
            yield val
        yield item
        first = False