from typer import Typer
from instances import s3_client

delete_file_from_bucket_command_handler = Typer()


@delete_file_from_bucket_command_handler.command()
def delete_file_from_bucket(bucket_name: str, file_name: str) -> None:
    s3_client.delete_object(Bucket=bucket_name, Key=file_name)
