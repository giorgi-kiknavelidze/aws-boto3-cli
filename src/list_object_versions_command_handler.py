from typer import Typer
from instances import s3_client

list_object_versions_command_handler = Typer()


@list_object_versions_command_handler.command()
def list_object_versions(bucket_name, file_name: str) -> None:
    response = s3_client.list_object_versions(Bucket=bucket_name, Prefix=file_name)
    versions = response["Versions"]

    print(len(versions))
    for version_data in versions:
        if version_data.get("LastModified") != None:
            print(version_data.get("LastModified"))
