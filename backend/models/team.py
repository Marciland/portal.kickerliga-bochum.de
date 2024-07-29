from pydantic import BaseModel


class TeamModel(BaseModel):
    name: str | None = None
    mk1: str
    mk2: str
    players: list[str]

    def get_full_team(self) -> list[str]:
        return [self.mk1, self.mk2] + self.players
