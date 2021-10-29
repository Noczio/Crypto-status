import os
from dataclasses import dataclass

import simplejson as json


@dataclass(frozen=True)
class JsonFile:
    path: str
    file_name: str

    def load(self) -> dict:
        try:
            final_path = f"{self.path}//{self.file_name}"
            with open(final_path, 'r', encoding="utf-8") as file:
                return json.load(file)
        except Exception as error:
            print(f"Load error: {error}")

    def save(self, data: dict) -> None:
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        try:
            final_path = f"{self.path}//{self.file_name}"
            with open(final_path, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except Exception as error:
            print(f"Save error: {error}")
