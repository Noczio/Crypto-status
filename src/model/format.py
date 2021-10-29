from decimal import Decimal
from re import sub


def format_table(data: list) -> tuple:
    current_price = Decimal(sub(r'[^\d\-.]', '', data[0].text))
    day_increase = Decimal(sub(r'[^\d\-.]', '', data[1].find_all("div")[-1].getText()))
    low_24 = Decimal(sub(r'[^\d\-.]', '', data[2].find_all("div")[0].getText().split(" ", 1)[0]))
    high_24 = Decimal(sub(r'[^\d\-.]', '', data[2].find_all("div")[-1].getText()))
    trading_volume_24h = Decimal(sub(r'[^\d\-.]', '', data[3].select_one("td > span").text))
    rank = int(data[6].text[1::])
    return current_price, day_increase, low_24, high_24, trading_volume_24h, rank
