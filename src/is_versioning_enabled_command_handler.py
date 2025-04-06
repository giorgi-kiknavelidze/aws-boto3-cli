from typer import Typer
from instances import s3_client

is_versioning_enabled_command_handler = Typer()


@is_versioning_enabled_command_handler.command()
def is_versioning_enabled(bucket_name: str) -> None:
    response = s3_client.get_bucket_versioning(Bucket=bucket_name)
    print(response.get("Status", "Disabled") == "Enabled")
