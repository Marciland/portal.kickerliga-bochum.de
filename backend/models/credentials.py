from pydantic import BaseModel


class EmailCreds(BaseModel):
    email: str
    password: str
