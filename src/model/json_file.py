import json
import os


class JsonFile:

    def __init__(self, path: str, file: str) -> None:
        self._path = path
        self._file = file

    def load(self) -> dict:
        final_path = f"{self._path}//{self._file}"
        with open(final_path, 'r', encoding="utf-8") as file:
            return json.load(file)

    def save(self, data: dict) -> None:
        if not os.path.exists(self._path):
            os.makedirs(self._path)

        final_path = f"{self._path}//{self._file}"
        with open(final_path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4)
