from instances import ec2_client


def add_security_group_rule(cidr: str, port: int, security_group_id: str) -> None:
    ec2_client.authorize_security_group_ingress(
        CidrIp=cidr,
        FromPort=port,
        GroupId=security_group_id,
        IpProtocol="tcp",
        ToPort=port,
    )
