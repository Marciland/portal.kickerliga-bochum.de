# pylint: skip-file
from unittest.mock import Mock
from io import StringIO
import csv
from models import TeamModel
from modules import dump_team_to_file


def test_dump_team_to_file():
    mock_team = Mock(spec=TeamModel)
    mock_team.name = "Test Team"
    mock_team.get_full_team.return_value = ["Player1", "Player2"]

    mock_file = StringIO()

    dump_team_to_file(mock_team, mock_file)

    mock_file.seek(0)
    reader = csv.reader(mock_file)
    rows = list(reader)

    assert len(rows) == 3
    assert rows[0] == ['Number', 'Name', 'Positions',
                       'Teams', 'Leagues', 'Seasons', 'Nationality']
    assert rows[1] == ['0', 'Player1', '', 'Test Team', '', '', '']
    assert rows[2] == ['1', 'Player2', '', 'Test Team', '', '', '']
