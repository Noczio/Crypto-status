from src.model.coin import Coin
from src.model.jsonfile import JsonFile
import requests
from bs4 import BeautifulSoup
from typing import List



class AppController:

    def load_disk_data(self, path: str, file: str) -> dict:
        web_data = JsonFile(path, file)
        return web_data.load()

    def scrape_web(self, link: list) -> List[Coin]:
        coins = []

        for url in link:
            web_request = requests.get(url)
            soup = BeautifulSoup(web_request.text, 'lxml')

            #name =
            #price =
            #day_change =
            #week_change =
            #market_cap =
            #volume =
            #suply =
            #current_coin = Coin(name, price, day_change, week_change, market_cap, volume, suply)
            #coins.append(current_coin)

        return coins


