class Seller:

    def __init__(self, id):
        self.id = id
        self.profit = 0.0
        self.market_prices = []

    def add_to_profit(self, profit):
        self.profit += profit

    def add_to_market_prices(self, value):
        self.market_prices.append(value);