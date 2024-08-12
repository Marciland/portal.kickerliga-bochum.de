# pylint: skip-file
from unittest.mock import AsyncMock

import jwt
import pytest
from fastapi import HTTPException, Request, status
from modules import Auth


@pytest.fixture
def auth():
    return Auth(key='secret_key')


@pytest.fixture
def mock_request():
    return AsyncMock(Request)


def test_Auth_login_success(auth: Auth):
    try:
        auth.login(password='secret_key')
    except HTTPException:
        pytest.fail('Login with same password should not raise!')


def test_Auth_login_failure(auth: Auth):
    with pytest.raises(HTTPException) as ex:
        auth.login(password='wrong_password')
    assert ex.value.status_code == status.HTTP_403_FORBIDDEN
    assert ex.value.detail == 'Ungültiges Passwort!'


@pytest.mark.asyncio
async def test_Auth_success(auth: Auth, mock_request):
    team = 'Team1'
    token = jwt.encode({'team': team},
                       'secret_key',
                       algorithm='HS256')
    mock_request.headers.get.return_value = f'Bearer {token}'

    result = await auth(mock_request)
    assert result == team


@pytest.mark.asyncio
async def test_Auth_missing_credentials(auth: Auth, mock_request):
    mock_request.headers.get.return_value = None

    with pytest.raises(HTTPException) as ex:
        await auth(mock_request)
    assert ex.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert ex.value.detail == 'Fehlende Autorisierung!'


@pytest.mark.asyncio
async def test_Auth_invalid_token(auth: Auth, mock_request):
    mock_request.headers.get.return_value = 'Bearer invalid.token'

    with pytest.raises(HTTPException) as ex:
        await auth(mock_request)
    assert ex.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert ex.value.detail == 'Ungültiges Token!'


@pytest.mark.asyncio
async def test_Auth_expired_token(auth: Auth, mock_request):
    expired_token = jwt.encode({'team': 'Team1',
                                'exp': 0},
                               'secret_key',
                               algorithm='HS256')
    mock_request.headers.get.return_value = f'Bearer {expired_token}'

    with pytest.raises(HTTPException) as ex:
        await auth(mock_request)
    assert ex.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert ex.value.detail == 'Token abgelaufen!'


@pytest.mark.asyncio
async def test_Auth_no_team_in_token(auth: Auth, mock_request):
    token_without_team = jwt.encode({},
                                    'secret_key',
                                    algorithm='HS256')
    mock_request.headers.get.return_value = f'Bearer {token_without_team}'

    with pytest.raises(HTTPException) as ex:
        await auth(mock_request)
    assert ex.value.status_code == status.HTTP_400_BAD_REQUEST
    assert ex.value.detail == 'Ungültiger Payload!'


def test_Auth_create_key(auth: Auth):
    payload = {'team': 'Team1'}
    token = auth.create_key(payload)
    decoded_payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
    assert decoded_payload == payload
