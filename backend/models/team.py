from fastapi import HTTPException, status
from pydantic import BaseModel


class TeamModel(BaseModel):
    name: str | None = None
    mk1: str
    mk2: str
    players: list[str]

    def check_validity(self) -> None:
        if self.name is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail='Das sollte nicht passieren!')
        players = self.get_full_team()
        if len(players) < 4:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='Zu wenig Spieler!')
        for name in players:
            # replace '-' if it should be allowed
            if not name.replace(' ', '').isalpha():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail='Ungültiger Name!')

    def get_full_team(self) -> list[str]:
        return [self.mk1, self.mk2] + self.players
