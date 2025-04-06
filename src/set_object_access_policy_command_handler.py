from typer import Typer
from instances import s3_client

set_object_access_policy_command_handler = Typer()


@set_object_access_policy_command_handler.command()
def set_object_access_policy(bucket_name: str, file_name: str):
    s3_client.put_object_acl(ACL="public-read", Bucket=bucket_name, Key=file_name)
