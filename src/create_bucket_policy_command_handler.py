from typer import Typer
from json import dumps
from instances import s3_client
from generate_public_read_policy import generate_public_read_policy

create_bucket_policy_command_handler = Typer()


@create_bucket_policy_command_handler.command()
def create_bucket_policy(bucket_name: str) -> None:
    s3_client.delete_public_access_block(Bucket=bucket_name)
    s3_client.put_bucket_policy(
        Bucket=bucket_name, Policy=generate_public_read_policy(bucket_name)
    )
