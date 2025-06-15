from typer import Typer, Option
from typing_extensions import Annotated
from instances import s3_client
from json import dumps
import requests

inspire_command_handler = Typer()

__api_endpoint = "https://api.quotable.kurokeita.dev/api/quotes/random"


@inspire_command_handler.command()
def inspire(
    author: Annotated[str, Option()] = "", save: Annotated[str, Option()] = ""
) -> None:
    params = {"author": author} if author != "" else None
    response = (
        requests.get(__api_endpoint, params=params)
        if params != None
        else requests.get(__api_endpoint)
    )
    response.raise_for_status()

    response_dict = response.json()

    print(response_dict["quote"]["content"])

    if save != "":
        s3_client.put_object(
            Bucket=save, Key="quote.json", Body=str(dumps(response_dict))
        )
