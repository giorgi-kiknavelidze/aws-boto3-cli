from instances import rds_client


def create_mysql_rds(
    security_group_id: str, name: str, username: str, password: str
) -> str:
    response = rds_client.create_db_instance(
        DBName="example",
        DBInstanceIdentifier=name,
        AllocatedStorage=60,
        DBInstanceClass="db.t4g.micro",
        Engine="mysql",
        MasterUsername=username,
        MasterUserPassword=password,
        VpcSecurityGroupIds=[security_group_id],
        PubliclyAccessible=True,
    )

    db_instance_id = response.get("DBInstance").get("DBInstanceIdentifier")
    if db_instance_id == None:
        raise Exception("missing db instance id")
    waiter = rds_client.get_waiter("db_instance_available")
    waiter.wait(DBInstanceIdentifier=db_instance_id)

    return db_instance_id
