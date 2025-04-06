from typer import Typer
from tempfile import TemporaryDirectory
from instances import s3_client
from os import path

rollback_s3_file_command_handler = Typer()


@rollback_s3_file_command_handler.command()
def rollback_s3_file(bucket_name: str, file_name: str) -> None:
    response = s3_client.list_object_versions(Bucket=bucket_name, Prefix=file_name)
    versions = response["Versions"]
    if len(versions) < 2:
        print("No second last version found")
    versions.sort(key=lambda v: v.get("LastModified", ""), reverse=True)
    second_last_version_id = versions[1].get("VersionId", "")

    with TemporaryDirectory() as tmp:
        tmp_file_name = path.join(tmp, "tmp.bin")
        s3_client.download_file(
            bucket_name,
            file_name,
            tmp_file_name,
            ExtraArgs={"VersionId": second_last_version_id},
        )
        s3_client.upload_file(Bucket=bucket_name, Key=file_name, Filename=tmp_file_name)
