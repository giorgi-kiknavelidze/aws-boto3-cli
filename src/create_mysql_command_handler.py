from typer import Typer
from getpass import getpass
from add_security_group_rule import add_security_group_rule
from create_security_group import create_security_group
from create_mysql_rds import create_mysql_rds

create_mysql_command_handler = Typer()


@create_mysql_command_handler.command()
def create_mysql(name: str, username: str) -> None:
    password = getpass()

    security_group_id = create_security_group(
        f"{name}-security-group", "MySql Security Group"
    )

    add_security_group_rule("0.0.0.0/0", 3306, security_group_id)

    create_mysql_rds(security_group_id, name, username, password)
