from os import getenv


def get_required_env(name: str) -> str:
    result = getenv(name)
    if result == None:
        raise ValueError(f"Expected {name} environment variable to be defined")
    return result
