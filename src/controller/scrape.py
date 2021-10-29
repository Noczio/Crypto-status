import requests
from bs4 import BeautifulSoup

from src.model.coin import Coin
from src.model.format import format_table
from src.model.json_file import JsonFile


def scrape_web(path: str, file: str) -> None:
    init_data = JsonFile(path, file)
    arguments = init_data.load()
    number_of_elements = len(arguments["search"])

    for index in range(number_of_elements):
        try:
            search_name = arguments["search"][index]
            web_request = requests.get(arguments["url"] + "/currencies/" + search_name)
            content = BeautifulSoup(web_request.content, 'lxml')
            table = content.findChildren('table')[0]
            rows = table.find_all('td')

            information = (search_name,) + format_table(rows)
            current_coin = Coin(*information)

            if index == number_of_elements - 1:
                print(current_coin)
            else:
                print(current_coin, end="\n\n")

            file = current_coin.time + ".json"
            path = "out/" + current_coin.name
            coin_info = current_coin.__dict__
            result = JsonFile(path, file)
            result.save(coin_info)
        except Exception as error:
            print(f"Error: {error}")
