from numpy import random
import config as cfg

if cfg.SEED:
    random.seed(cfg.SEED)

class Seller:

    def __init__(self, id, strategy):
        self.id = id
        self.profit = 0.0
        self.market_prices = []
        self.strategy = strategy


    def uniform_closed(self, a, b):
        while True:
            r = random.uniform(a, b)  # range [a, b)
            if r > a: return r  # range (a, b)


    def init_random_starting_price(self, max_price):
        starting_price = self.uniform_closed(0, max_price)
        if self.strategy:
            starting_price = max_price
        return starting_price


    def add_to_profit(self, profit):
        self.profit += profit


    def add_to_market_prices(self, value):
        self.market_prices.append(value);

