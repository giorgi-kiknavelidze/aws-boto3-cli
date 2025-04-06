from aws_config import AWSConfig
from create_s3_client import create_s3_client

aws_config = AWSConfig()
s3_client = create_s3_client(aws_config)
