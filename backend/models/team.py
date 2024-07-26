from pydantic import BaseModel


class TeamModel(BaseModel):
    mk1: str
    mk2: str
    players: list[str]
