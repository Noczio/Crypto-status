from src.model.coin import Coin
from src.model.format import format_crypto_data
from src.model.jsonfile import JsonFile
import requests
from bs4 import BeautifulSoup
from typing import List


class AppController:

    def load_disk_data(self, path: str, file: str) -> dict:
        web_data = JsonFile(path, file)
        return web_data.load()

    def scrape_web(self, url: str, search: List[str]) -> List[Coin]:
        information = []

        for name in search:
            web_request = requests.get(url + "/currencies/" + name)
            content = BeautifulSoup(web_request.content, 'lxml')
            table = content.findChildren('table')[0]

            for row in table.find_all('tr'):
                columns = row.find_all('td')

            """
            info_formatted = format_crypto_data(price, hour_change, day_change,
                                                week_change, market_cap, volume, supply)
    
            current_coin = Coin(name, *info_formatted)
            information.append(current_coin)
            """

        return information


