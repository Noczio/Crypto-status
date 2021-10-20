from typing import Iterator, List

import requests
from bs4 import BeautifulSoup

from src.model.coin import Coin
from src.model.format import format_table
from src.model.json_file import JsonFile


class AppController:

    def load_disk_data(self, path: str, file: str) -> dict:
        web_data = JsonFile(path, file)
        return web_data.load()

    def scrape_web(self, url: str, search: List[str]) -> Iterator[Coin]:
        for name in search:
            web_request = requests.get(url + "/currencies/" + name)
            content = BeautifulSoup(web_request.content, 'lxml')
            table = content.findChildren('table')[0]
            rows = table.find_all('td')
            information = format_table(rows)
            yield Coin(name, *information)
