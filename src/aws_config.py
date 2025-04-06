from dotenv import load_dotenv
from get_required_env import get_required_env


class AWSConfig:
    def __init__(self):
        load_dotenv()
        self.__aws_region_name = get_required_env("aws_region_name")
        self.__aws_access_key_id = get_required_env("aws_access_key_id")
        self.__aws_secret_access_key = get_required_env("aws_secret_access_key")
        self.__aws_session_token = get_required_env("aws_session_token")

    @property
    def aws_region_name(self):
        return self.__aws_region_name

    @property
    def aws_access_key_id(self):
        return self.__aws_access_key_id

    @property
    def aws_secret_access_key(self):
        return self.__aws_secret_access_key

    @property
    def aws_session_token(self):
        return self.__aws_session_token
