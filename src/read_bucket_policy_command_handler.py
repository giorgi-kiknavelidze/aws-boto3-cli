from typer import Typer
from instances import s3_client

read_bucket_policy_command_handler = Typer()


@read_bucket_policy_command_handler.command()
def read_bucket_policy(bucket_name: str):
    response = s3_client.get_bucket_policy(Bucket=bucket_name)
    policy = response["Policy"]
    print(policy)
