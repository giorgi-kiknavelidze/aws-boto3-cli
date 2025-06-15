from instances import ec2_client


def create_security_group(group_name: str, description: str) -> str:
    response = ec2_client.create_security_group(
        Description=description, GroupName=group_name
    )
    group_id = response.get("GroupId")
    waiter = ec2_client.get_waiter("security_group_exists")
    waiter.wait(GroupIds=[group_id])

    return group_id
