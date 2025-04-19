from typer import Typer
from mimetypes import guess_extension
from get_file_mime import get_file_mime
from upload_file_to_bucket_command_handler import upload_file_to_bucket

organized_upload_file_to_bucket_command_handler = Typer()


@organized_upload_file_to_bucket_command_handler.command()
def organized_upload_file_to_bucket(bucket_name: str, src: str, dest: str) -> None:
    with open(src, "rb") as file:
        mime_type = get_file_mime(file.read())
        file_extension = guess_extension(mime_type)
        upload_file_to_bucket(
            bucket_name,
            src,
            f"{file_extension if file_extension is None else "" }/{dest}",
        )
