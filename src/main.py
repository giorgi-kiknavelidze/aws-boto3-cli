from typer import Typer
from logging import error
from create_bucket_command_handler import create_bucket_command_handler
from create_bucket_policy_command_handler import create_bucket_policy_command_handler
from delete_bucket_command_handler import delete_bucket_command_handler
from exists_bucket_command_handler import exists_bucket_command_handler
from list_buckets_command_handler import list_buckets_command_handler
from read_bucket_policy_command_handler import read_bucket_policy_command_handler
import rollback_s3_file_command_handler
from set_object_access_policy_command_handler import (
    set_object_access_policy_command_handler,
)
from download_and_upload_to_bucket_command_handler import (
    download_and_upload_to_bucket_command_handler,
)
from delete_file_from_bucket_command_handler import (
    delete_file_from_bucket_command_handler,
)
from upload_file_to_bucket_command_handler import upload_file_to_bucket_command_handler
from upload_multipart_file_to_bucket_command_handler import (
    upload_multipart_file_to_bucket_command_handler,
)
from configure_lifecycle_policy_command_handler import (
    configure_lifecycle_policy_command_handler,
)
from organize_bucket_command_handler import organize_bucket_command_handler
from is_versioning_enabled_command_handler import is_versioning_enabled_command_handler
from rollback_s3_file_command_handler import rollback_s3_file_command_handler
from list_object_versions_command_handler import list_object_versions_command_handler
from organized_upload_file_to_bucket_command_handler import (
    organized_upload_file_to_bucket_command_handler,
)
from delete_old_versions_command_handler import delete_old_versions_command_handler


def main() -> None:
    app = Typer()
    app.add_typer(create_bucket_command_handler)
    app.add_typer(create_bucket_policy_command_handler)
    app.add_typer(delete_bucket_command_handler)
    app.add_typer(exists_bucket_command_handler)
    app.add_typer(list_buckets_command_handler)
    app.add_typer(read_bucket_policy_command_handler)
    app.add_typer(set_object_access_policy_command_handler)
    app.add_typer(download_and_upload_to_bucket_command_handler)
    app.add_typer(delete_file_from_bucket_command_handler)
    app.add_typer(upload_file_to_bucket_command_handler)
    app.add_typer(upload_multipart_file_to_bucket_command_handler)
    app.add_typer(configure_lifecycle_policy_command_handler)
    app.add_typer(organize_bucket_command_handler)
    app.add_typer(is_versioning_enabled_command_handler)
    app.add_typer(list_object_versions_command_handler)
    app.add_typer(rollback_s3_file_command_handler)
    app.add_typer(organized_upload_file_to_bucket_command_handler)
    app.add_typer(delete_old_versions_command_handler)

    try:
        app()
    except Exception as e:
        error(str(e))


main()
