from datetime import datetime

from colorama import Fore


class Coin:

    def __init__(self, name: str, current_price: str, day_increase: str, low_price: str,
                 high_price: str, trading_volume: str, rank: str):
        self.name = name
        self.current_price = current_price
        self.day_increase = day_increase
        self.low_price = low_price
        self.high_price = high_price
        self.trading_volume = trading_volume
        self.rank = rank
        self.time = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

    def __str__(self) -> str:
        return f"{Fore.YELLOW}{self.name}{Fore.RESET} at {Fore.BLUE}{self.time}{Fore.RESET} " \
               f"has a price of {Fore.GREEN}{self.current_price}{Fore.RESET} USD" \
               f"\nLowest price is {Fore.GREEN}{self.low_price}{Fore.RESET} USD and " \
               f"highest price is {Fore.GREEN}{self.high_price}{Fore.RESET} USD " \
               f"with a day change of {Fore.CYAN}{self.day_increase}{Fore.RESET}" \
               f"\nTrading volume is {Fore.GREEN}{self.trading_volume}{Fore.RESET} USD " \
               f"and its currently ranked {Fore.RED}{self.rank}{Fore.RESET}"
