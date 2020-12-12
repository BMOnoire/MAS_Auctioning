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
        self.previous_market_price = 0
        self.previous_starting_price = 0
        self.previous_auction_price = 0


    def uniform_closed(self, a, b):
        while True:
            r = random.uniform(a, b)  # range [a, b)
            if r > a: return r  # range (a, b)


    def init_random_starting_price(self, max_price):
        starting_price = self.uniform_closed(0, max_price)
        if self.strategy=="OWN":
            starting_price = max_price
        elif self.strategy == "COM":
            if self.previous_starting_price == 0 and self.previous_market_price == 0 and self.previous_auction_price == 0:
                starting_price = self.uniform_closed(0, max_price)
            else:
                buyer_profit = self.previous_market_price - self.previous_auction_price
                starting_price = self.previous_auction_price - buyer_profit
        print("starting", starting_price)
        return starting_price

    def add_to_profit(self, profit):
        self.profit += profit


    def add_to_market_prices(self, value):
        self.market_prices.append(value);

