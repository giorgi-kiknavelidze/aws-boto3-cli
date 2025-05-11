from typer import Typer
from os import listdir, fsdecode
from os.path import isfile, isdir, join
from pathlib import Path

from types_boto3_s3.type_defs import WebsiteConfigurationTypeDef
from create_bucket_command_handler import create_bucket
from create_bucket_policy_command_handler import create_bucket_policy
from upload_file_to_bucket_command_handler import upload_file_to_bucket
from instances import s3_client

host_static_site_command_handler = Typer()


def __recursive_upload_to_bucket(
    bucket_name: str, source: str, prefix: str, is_root: bool
):
    if isfile(source):
        upload_file_to_bucket(
            bucket_name, source, f"{prefix}/{Path(source).name}".lstrip("/")
        )
    elif isdir(source):
        for file in listdir(source):
            filename = fsdecode(file)

            __recursive_upload_to_bucket(
                bucket_name,
                join(source, filename),
                "" if is_root else f"{prefix}/{Path(source).name}",
                False,
            )


@host_static_site_command_handler.command()
def host_static_site(bucket_name: str, source: str, print_url: bool = True) -> None:
    create_bucket(bucket_name)
    create_bucket_policy(bucket_name)

    website_configuration: WebsiteConfigurationTypeDef = {
        "ErrorDocument": {"Key": "error.html"},
        "IndexDocument": {"Suffix": "index.html"},
    }

    s3_client.put_bucket_website(
        Bucket=bucket_name, WebsiteConfiguration=website_configuration
    )
    __recursive_upload_to_bucket(bucket_name, source, "", True)
    if print_url:
        print(f"http://{bucket_name}.s3-website-us-west-2.amazonaws.com/")
