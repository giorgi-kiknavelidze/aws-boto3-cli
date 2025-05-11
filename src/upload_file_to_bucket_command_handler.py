from typer import Typer
from instances import s3_client
from get_file_mime import get_file_mime

upload_file_to_bucket_command_handler = Typer()


@upload_file_to_bucket_command_handler.command()
def upload_file_to_bucket(bucket_name: str, src: str, dest: str) -> None:
    with open(src, "rb") as f:
        src_bytes = f.read()

    s3_client.upload_file(
        src, bucket_name, dest, ExtraArgs={"ContentType": get_file_mime(src_bytes)}
    )
