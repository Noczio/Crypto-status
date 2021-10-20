import requests
from bs4 import BeautifulSoup

from src.model.coin import Coin
from src.model.format import format_table
from src.model.json_file import JsonFile


class AppController:

    def __init__(self, path: str, file: str) -> None:
        json_data = JsonFile(path, file)
        self.arguments = json_data.load()

    def scrape_web(self) -> None:
        number_of_elements = len(self.arguments["search"])

        for index in range(number_of_elements):
            search_name = self.arguments["search"][index]
            web_request = requests.get(self.arguments["url"] + "/currencies/" + search_name)
            content = BeautifulSoup(web_request.content, 'lxml')
            table = content.findChildren('table')[0]
            rows = table.find_all('td')

            information = format_table(rows)
            current_coin = Coin(search_name, *information)

            if index == number_of_elements - 1:
                print(current_coin)
            else:
                print(current_coin, end="\n\n")

            file_name = current_coin.time + ".json"
            path = "out/" + current_coin.name
            result = JsonFile(path, file_name)
            result.save(current_coin.__dict__)
