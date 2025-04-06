from typer import Typer
from instances import s3_client

list_buckets_command_handler = Typer()


@list_buckets_command_handler.command()
def list_buckets():
    response = s3_client.list_buckets()
    bucket_names = [x.get("Name") for x in response["Buckets"]]
    for bucket_name in bucket_names:
        print(bucket_name)
