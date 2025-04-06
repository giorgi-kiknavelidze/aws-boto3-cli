from boto3 import client
from aws_config import AWSConfig
from types_boto3_s3 import S3Client


def create_s3_client(config: AWSConfig) -> S3Client:
    return client(
        "s3",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key,
        aws_session_token=config.aws_session_token,
        region_name=config.aws_region_name,
    )
