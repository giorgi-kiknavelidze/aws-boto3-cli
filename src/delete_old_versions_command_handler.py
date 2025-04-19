from typer import Typer
from datetime import datetime
from dateutil.relativedelta import relativedelta
from instances import s3_client

delete_old_versions_command_handler = Typer()


def delete_old_version_for_file(bucket_name: str, file_name: str) -> None:
    version_data = s3_client.list_object_versions(Bucket=bucket_name, Prefix=file_name)
    six_months_ago = datetime.now() - relativedelta(months=6)
    for version in version_data["Versions"]:
        is_version_latest = version.get("IsLatest")
        if is_version_latest:
            continue
        last_modified = version.get("LastModified")
        version_id = version.get("VersionId")
        if version_id == None or last_modified == None:
            continue
        if last_modified.date() <= six_months_ago.date():
            s3_client.delete_object(
                Bucket=bucket_name, Key=file_name, VersionId=version_id
            )


@delete_old_versions_command_handler.command()
def delete_old_versions(bucket_name: str, file_names: list[str]) -> None:
    for file_name in file_names:
        delete_old_version_for_file(bucket_name, file_name)
