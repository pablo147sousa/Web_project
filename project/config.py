from os import environ
from pydantic import BaseModel, SecretStr

class BaseConfig(BaseModel):
    SECRET_KEY: SecretStr
    DEBUG:bool


__setup = dict(
    DEV=BaseConfig(
        SECRET_KEY=SecretStr(environ["SECRET_KEY"]),
        DEBUG=True
    ),
    PROD=BaseConfig(
        SECRET_KEY=SecretStr(environ["SECRET_KEY"]),
        DEBUG=False
    )
)
config:BaseConfig = __setup[environ["ENV"]]
