# pylint: skip-file
import pytest
from models import TeamModel
from fastapi import HTTPException


@pytest.mark.parametrize('name, mk1, mk2, players, valid, exception', [
    ('Valid Teamname', 'Valid MK', 'Valid MKTwo',
     ['Some Player', 'Another Player'], True, None),
    (None, 'Valid MK', 'Valid MKTwo',
     ['Some Player', 'Another Player'], False, 'Name fehlt'),
    ('Valid Teamname', 'Invalid MK1', 'Valid MKTwo',
     ['Some Player', 'Another Player'], False, 'Ungültiger Spielername: Invalid MK1'),
    ('Valid Teamname', 'Valid MK', 'Valid MKTwo',
     ['Some Player', 'Invalid Play3r'], False, 'Ungültiger Spielername: Invalid Play3r'),
    ('Valid Teamname', 'Valid MK', 'Valid MKTwo',
     ['Some Player'], False, 'Zu wenig Spieler!'),
])
def test_TeamModel_check_validity(name, mk1, mk2, players, valid, exception):
    team = TeamModel(name=name, mk1=mk1, mk2=mk2, players=players)
    if not valid:
        with pytest.raises(HTTPException) as ex:
            team.check_validity()
        assert exception in str(ex)
    else:
        try:
            team.check_validity()
        except HTTPException as ex:
            pytest.fail(ex)


@pytest.mark.parametrize('name, mk1, mk2, players, expected', [
    ('Any Teamname', 'Any MK', 'Any Other MK',
     ['Some Player'], ['Any MK', 'Any Other MK', 'Some Player'])
])
def test_TeamModel_get_full_team(name, mk1, mk2, players, expected):
    team = TeamModel(name=name, mk1=mk1, mk2=mk2, players=players)
    assert team.get_full_team() == expected
