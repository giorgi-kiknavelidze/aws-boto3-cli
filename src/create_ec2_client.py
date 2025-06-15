from boto3 import client
from aws_config import AWSConfig
from types_boto3_ec2 import EC2Client


def create_ec2_client(config: AWSConfig) -> EC2Client:
    return client(
        "ec2",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key,
        aws_session_token=config.aws_session_token,
        region_name=config.aws_region_name,
    )
