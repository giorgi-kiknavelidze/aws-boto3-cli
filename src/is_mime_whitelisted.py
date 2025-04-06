whitelisted_mimes = ["image/bmp", "image/jpeg", "image/png", "image/webp", "video/mp4"]


def is_mime_whitelisted(mimetype: str) -> bool:
    return mimetype in whitelisted_mimes
