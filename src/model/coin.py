class Coin:
    _name: str
    _price: float
    _day_change: float
    _week_change: float
    _market_cap: float
    _volume: float
    _supply: float

    def __init__(self, name: str = 'coin', price: float = 0, day_change: float = 0, week_change: float = 0,
                 market_cap: float = 0, volume: float = 0, supply: float = 0):
        self.name = name
        self.price = price
        self.day_change = day_change
        self.week_change = week_change
        self.market_cap = market_cap
        self.volume = volume
        self.supply = supply

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def day_change(self):
        return self._day_change

    @day_change.setter
    def day_change(self, value: float):
        self._day_change = value

    @property
    def week_change(self):
        return self._week_change

    @week_change.setter
    def week_change(self, value: float):
        self._week_change = value

    @property
    def market_cap(self):
        return self._market_cap

    @market_cap.setter
    def market_cap(self, value: float):
        self._market_cap = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def supply(self):
        return self._supply

    @supply.setter
    def supply(self, value: float):
        self._supply = value
