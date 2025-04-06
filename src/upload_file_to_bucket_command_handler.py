from typer import Typer
from instances import s3_client

upload_file_to_bucket_command_handler = Typer()


@upload_file_to_bucket_command_handler.command()
def upload_file_to_bucket(bucket_name: str, src: str, dest: str) -> None:
    s3_client.upload_file(src, bucket_name, dest)
