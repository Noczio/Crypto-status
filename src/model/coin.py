from datetime import datetime

from colorama import Fore


class Coin:
    _name: str
    _price: float
    _hour_change: float
    _day_change: float
    _week_change: float
    _market_cap: float
    _volume: float
    _supply: float
    _time: str

    def __init__(self, name: str = 'coin', price: float = 0, hour_change: float = 0, day_change: float = 0, week_change: float = 0,
                 market_cap: float = 0, volume: float = 0, supply: float = 0):
        self.name = name
        self.price = price
        self.hour_change = hour_change
        self.day_change = day_change
        self.week_change = week_change
        self.market_cap = market_cap
        self.volume = volume
        self.supply = supply
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        self._price = value

    @property
    def hour_change(self) -> float:
        return self._hour_change

    @hour_change.setter
    def hour_change(self, value: float) -> None:
        self._hour_change = value

    @property
    def day_change(self) -> float:
        return self._day_change

    @day_change.setter
    def day_change(self, value: float) -> None:
        self._day_change = value

    @property
    def week_change(self) -> float:
        return self._week_change

    @week_change.setter
    def week_change(self, value: float) -> None:
        self._week_change = value

    @property
    def market_cap(self) -> float:
        return self._market_cap

    @market_cap.setter
    def market_cap(self, value: float) -> None:
        self._market_cap = value

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, value: float) -> None:
        self._volume = value

    @property
    def supply(self) -> float:
        return self._supply

    @supply.setter
    def supply(self, value: float) -> None:
        self._supply = value

    @property
    def time(self) -> str:
        return self._time

    @time.setter
    def time(self, value: str) -> None:
        self._time = value

    def __str__(self) -> str:
        return f"{Fore.YELLOW}{self.name}{Fore.RESET} at {Fore.BLUE}{self.time}{Fore.RESET} " \
               f"has a current price of {Fore.GREEN}${self.price}{Fore.RESET} USD" \
               f"\nDaily change is {Fore.CYAN}{self.day_change:.2f}%{Fore.RESET} " \
               f"week change is {Fore.CYAN}{self.day_change:.2f}%{Fore.RESET} and " \
               f"hour change is {Fore.CYAN}{self.hour_change:.2f}%{Fore.RESET}" \
               f"\nCoin volume is {Fore.GREEN}${self.volume}{Fore.RESET} USD " \
               f"and its circulation supply is {Fore.RED}{self.supply}{Fore.RESET}"
