from numpy import random

class Seller:

    def __init__(self, id):
        self.id = id
        self.profit = 0.0
        self.market_prices = []


    def uniform_closed(self, a, b):
        while True:
            r = random.uniform(a, b)  # range [a, b)
            if r > a: return r  # range (a, b)


    def init_random_starting_price(self, max_price):
        return self.uniform_closed(0, max_price)


    def add_to_profit(self, profit):
        self.profit += profit






    def add_to_market_prices(self, value):
        self.market_prices.append(value);

