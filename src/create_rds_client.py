from boto3 import client
from aws_config import AWSConfig
from types_boto3_rds import RDSClient


def create_rds_client(config: AWSConfig) -> RDSClient:
    return client(
        "rds",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key,
        aws_session_token=config.aws_session_token,
        region_name=config.aws_region_name,
    )
