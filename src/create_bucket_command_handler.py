from typer import Typer
from instances import s3_client

create_bucket_command_handler = Typer()


@create_bucket_command_handler.command()
def create_bucket(bucket_name: str) -> None:
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": "us-west-2"},
    )
