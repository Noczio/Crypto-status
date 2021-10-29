from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from colorama import Fore


@dataclass(frozen=True)
class Coin:
    name: str
    current_price: Decimal
    day_increase: Decimal
    low_price: Decimal
    high_price: Decimal
    trading_volume: Decimal
    rank: int
    time: str = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

    def __str__(self) -> str:
        return f"{Fore.YELLOW}{self.name}{Fore.RESET} at {Fore.BLUE}{self.time}{Fore.RESET} " \
               f"has a price of {Fore.GREEN}${self.current_price}{Fore.RESET} USD" \
               f"\nLowest price is {Fore.GREEN}${self.low_price}{Fore.RESET} USD and " \
               f"highest price is {Fore.GREEN}${self.high_price}{Fore.RESET} USD " \
               f"with a day change of {Fore.CYAN}{self.day_increase}{Fore.RESET}" \
               f"\nTrading volume is {Fore.GREEN}${self.trading_volume}{Fore.RESET} USD " \
               f"and its currently ranked {Fore.RED}#{self.rank}{Fore.RESET}"
