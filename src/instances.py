from aws_config import AWSConfig
from create_s3_client import create_s3_client
from create_rds_client import create_rds_client
from create_ec2_client import create_ec2_client

aws_config = AWSConfig()
s3_client = create_s3_client(aws_config)
rds_client = create_rds_client(aws_config)
ec2_client = create_ec2_client(aws_config)
