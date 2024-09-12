# pylint: skip-file
from unittest.mock import mock_open, patch

import pytest
from modules import read_json


@pytest.mark.parametrize('file_data, expected', [
    ('', {}),
    ('{"key": "value"}', {'key': 'value'})
])
def test_read_json(file_data, expected):
    file_path = 'any file'
    with patch('builtins.open', mock_open(read_data=file_data)):
        json = read_json(file_path)
    assert json == expected
