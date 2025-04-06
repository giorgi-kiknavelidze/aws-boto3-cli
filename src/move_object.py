from instances import s3_client


def move_object(bucket_name: str, src: str, dest: str) -> None:
    s3_client.copy_object(
        Bucket=bucket_name, CopySource={"Bucket": bucket_name, "Key": src}, Key=dest
    )
    s3_client.delete_object(Bucket=bucket_name, Key=src)
