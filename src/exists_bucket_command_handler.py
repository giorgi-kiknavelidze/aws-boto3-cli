from typer import Typer
from instances import s3_client

exists_bucket_command_handler = Typer()


@exists_bucket_command_handler.command()
def exists_bucket(bucket_name):
    try:
        response = s3_client.head_bucket(Bucket=bucket_name)
        status_code = response["ResponseMetadata"]["HTTPStatusCode"]
        if status_code == 200:
            print("True")
        else:
            print("False")
    except Exception:
        print("False")
