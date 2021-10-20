from datetime import datetime

from colorama import Fore


class Coin:

    def __init__(self, name: str, price: str, day_change: str,
                 week_change: str, market_cap: str, volume: str, supply: str):
        self.name = name
        self.price = price
        self.day_change = day_change
        self.week_change = week_change
        self.market_cap = market_cap
        self.volume = volume
        self.supply = supply
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self) -> str:
        return f"{Fore.YELLOW}{self.name}{Fore.RESET} at {Fore.BLUE}{self.time}{Fore.RESET} " \
               f"has a price of {Fore.GREEN}{self.price}{Fore.RESET} USD" \
               f"\n24h change is {Fore.CYAN}{self.day_change}{Fore.RESET} and " \
               f"week change is {Fore.CYAN}{self.day_change}{Fore.RESET} " \
               f"\nCoin volume is {Fore.GREEN}{self.volume}{Fore.RESET} USD " \
               f"and its circulation supply is {Fore.RED}{self.supply}{Fore.RESET}"
