from os import environ
from pydantic import BaseModel, SecretStr
from typing import Literal, TypeAlias

db_config: TypeAlias = dict[Literal["ENGINE", "NAME", "USER", "PASSWORD", "HOST", "PORT"], str]


class BaseConfig(BaseModel):
    SECRET_KEY: SecretStr
    DEBUG:bool
    DB_ENGINE: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    def get_db_config(self) -> db_config:
        return {
            "ENGINE": self.DB_ENGINE,
            "NAME": self.DB_NAME,
            "USER": self.DB_USER,
            "PASSWORD": self.DB_PASSWORD,
            "HOST": self.DB_HOST,
            "PORT": self.DB_PORT,
        }


__setup = dict(
    DEV=BaseConfig(
        SECRET_KEY=SecretStr(environ["SECRET_KEY"]),
        DEBUG=True,
        DB_ENGINE=environ["DB_ENGINE"],
        DB_NAME=environ["DB_NAME"],
        DB_USER=environ["DB_USER"],
        DB_PASSWORD=environ["DB_PASSWORD"],
        DB_HOST=environ["DB_HOST"],
        DB_PORT=environ["DB_PORT"],
    ),
    STAGING=BaseConfig(
        SECRET_KEY=SecretStr(environ["SECRET_KEY"]),
        DEBUG=True,
        DB_ENGINE=environ["DB_ENGINE"],
        DB_NAME=environ["DB_NAME"],
        DB_USER=environ["DB_USER"],
        DB_PASSWORD=environ["DB_PASSWORD"],
        DB_HOST=environ["DB_HOST"],
        DB_PORT=environ["DB_PORT"],
    ),
    PROD=BaseConfig(
        SECRET_KEY=SecretStr(environ["SECRET_KEY"]),
        DEBUG=False,
        DB_ENGINE=environ["DB_ENGINE"],
        DB_NAME=environ["DB_NAME"],
        DB_USER=environ["DB_USER"],
        DB_PASSWORD=environ["DB_PASSWORD"],
        DB_HOST=environ["DB_HOST"],
        DB_PORT=environ["DB_PORT"],
    )
)

config:BaseConfig = __setup[environ["ENV"]]
