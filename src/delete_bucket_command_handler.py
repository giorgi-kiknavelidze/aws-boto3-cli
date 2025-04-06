from typer import Typer
from instances import s3_client

delete_bucket_command_handler = Typer()


@delete_bucket_command_handler.command()
def delete_bucket(bucket_name: str):
    s3_client.delete_bucket(Bucket=bucket_name)
