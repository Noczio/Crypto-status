def format_crypto_data(price: str, hour_change: str, day_change: str, week_change: str,
                       market_cap: str, volume: str, supply: str) -> tuple:
    formatted_price = float(price[1::])
    formatted_hour_change = float(hour_change[:-1:])
    formatted_day_change = float(day_change[:-1:])
    formatted_week_change = float(week_change[:-1:])
    formatted_market_cap = float(market_cap[1::])
    formatted_volume = float(volume[1::])
    supply_split = supply.split(" ")
    formatted_supply = float(supply_split[0])

    return (formatted_price, formatted_hour_change, formatted_day_change, formatted_week_change,
            formatted_market_cap, formatted_volume, formatted_supply)
