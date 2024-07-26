import jwt
from fastapi import HTTPException, Request, status
from fastapi.security import HTTPBearer
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError


class Auth(HTTPBearer):
    def __init__(self, key: str):
        self.key = key
        # https://github.com/tiangolo/fastapi/issues/10177
        # set auto_error=True if this is fixed
        super().__init__(auto_error=False)

    async def __call__(self, request: Request) -> str:
        credentials = await super().__call__(request)
        if not credentials:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Fehlende Autorisierung!')
        if not credentials.scheme == 'Bearer':
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Ungültiges Schema!')
        try:
            return jwt.decode(credentials.credentials, self.key, algorithms=['HS256'])
        except ExpiredSignatureError as ex:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Token abgelaufen!') from ex
        except InvalidTokenError as ex:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Ungültiges Token!') from ex

    def login(self, password: str):
        if not password == self.key:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail='Ungültiges Passwort!')

    def create_key(self, payload: dict) -> str:
        return jwt.encode(payload, self.key, algorithm='HS256')
