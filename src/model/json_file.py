import json


class JsonFile:

    def __init__(self, path: str, file: str) -> None:
        self._path = path
        self._file = file

    def load(self) -> dict:
        final_path = self._path + "\\" + self._file
        with open(final_path, 'r', encoding="utf-8") as file:
            return json.load(file)

    def save(self, data: dict) -> None:
        final_path = self._path + "\\" + self._file
        with open(final_path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=2)
