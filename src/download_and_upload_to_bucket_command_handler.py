from typer import Typer
from urllib.request import urlopen
from io import BytesIO
from instances import s3_client
from get_file_mime import get_file_mime
from is_mime_whitelisted import is_mime_whitelisted

download_and_upload_to_bucket_command_handler = Typer()


@download_and_upload_to_bucket_command_handler.command()
def download_and_upload_to_bucket(bucket_name: str, url: str, file_name: str) -> None:
    with urlopen(url) as response:
        content = response.read()
        mime = get_file_mime(content)
        if not is_mime_whitelisted(mime):
            raise Exception("filetype not supported")

        s3_client.upload_fileobj(
            Fileobj=BytesIO(content),
            Bucket=bucket_name,
            ExtraArgs={"ContentType": mime},
            Key=file_name,
        )

    print(f"https://s3-us-west-2.amazonaws.com/{bucket_name}/{file_name}")
