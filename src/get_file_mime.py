from magic import from_buffer


def get_file_mime(buffer: bytes) -> str:
    return from_buffer(buffer, mime=True)
