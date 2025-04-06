from instances import s3_client


def get_bucket_objects(bucket_name: str):
    result: list[str] = []
    response = s3_client.list_objects(Bucket=bucket_name)
    for object in response.get("Contents", []):
        object_name = object.get("Key")
        if object_name != None:
            result.append(object_name)
    return result
