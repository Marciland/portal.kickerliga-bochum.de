from json import load
from json.decoder import JSONDecodeError


def read_json(file_path: str) -> dict:
    with open(file=file_path, mode='r', encoding='utf-8') as file_handle:
        try:
            json: dict = load(file_handle)
        except JSONDecodeError:
            return {}
    return json
