def format_table(data: list) -> tuple:
    current_price = data[0].text
    day_increase = data[1].find_all("div")[-1].getText()
    low_24 = data[2].find_all("div")[0].getText().split(" ", 1)[0]
    high_24 = data[2].find_all("div")[-1].getText()
    trading_volume_24h = data[3].select_one("td > span").text
    rank = data[6].text
    return current_price, day_increase, low_24, high_24, trading_volume_24h, rank

