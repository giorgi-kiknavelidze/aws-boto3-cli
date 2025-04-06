from typer import Typer
from os import stat
from instances import s3_client

upload_multipart_file_to_bucket_command_handler = Typer()


@upload_multipart_file_to_bucket_command_handler.command()
def upload_multipart_file_to_bucket(bucket_name: str, src: str, dest: str) -> None:
    multi_part_upload = s3_client.create_multipart_upload(Bucket=bucket_name, Key=dest)
    multi_part_upload_id = multi_part_upload["UploadId"]

    parts = []
    uploaded_bytes = 0
    total_bytes = stat(src).st_size
    with open(src, "rb") as file:
        part_counter = 1
        while True:
            file_content = file.read(1024)
            if not len(file_content):
                break
            part = s3_client.upload_part(
                Body=file_content,
                Bucket=bucket_name,
                Key=dest,
                UploadId=multi_part_upload_id,
                PartNumber=part_counter,
            )
            parts.append({"PartNumber": part_counter, "ETag": part["ETag"]})
            part_counter += 1
            uploaded_bytes += len(file_content)
            print(f"uploaded {uploaded_bytes} of {total_bytes}")
    s3_client.complete_multipart_upload(
        Bucket=bucket_name,
        Key=dest,
        UploadId=multi_part_upload_id,
        MultipartUpload={"Parts": parts},
    )
