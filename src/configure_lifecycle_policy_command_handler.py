from typer import Typer
from types_boto3_s3.type_defs import BucketLifecycleConfigurationTypeDef
from instances import s3_client

configure_lifecycle_policy_command_handler = Typer()


@configure_lifecycle_policy_command_handler.command()
def configure_lifecycle_policy(bucket_name) -> None:
    configuration: BucketLifecycleConfigurationTypeDef = {
        "Rules": [
            {
                "Expiration": {"Days": 120},
                "ID": "Expiration Policy",
                "Filter": {"Prefix": ""},
                "Status": "Enabled",
            }
        ]
    }

    s3_client.put_bucket_lifecycle_configuration(
        Bucket=bucket_name, LifecycleConfiguration=configuration
    )
