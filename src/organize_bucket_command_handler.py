from typer import Typer
from pathlib import Path
from get_bucket_objects import get_bucket_objects
from move_object import move_object

organize_bucket_command_handler = Typer()


@organize_bucket_command_handler.command()
def organize_bucket(bucket_name: str) -> None:
    objects = get_bucket_objects(bucket_name)
    suffix_dict: dict[str, int] = {}
    for object in objects:
        if "/" in object:
            continue
        if not ("." in object):
            continue
        suffix = Path(object).suffix[1:]
        suffix_dict[suffix] = (
            suffix_dict[suffix] + 1 if suffix_dict.get(suffix) != None else 1
        )
        move_object(bucket_name, object, f"{suffix}/{object}")
    for key in suffix_dict:
        print(f"{key} - {suffix_dict[key]}")
