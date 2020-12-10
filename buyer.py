import random
import config as cfg
from numpy import random

if cfg.SEED:
    random.seed(cfg.SEED)

class Buyer:

    def __init__(self, id, seller_list, bidding_factor_max, range_bidding_factor_increase, range_bidding_factor_decrease):
        self.id = id
        self.profit = 0.0
        self.bidding_factor_max = bidding_factor_max
        self.bidding_factor_list = { slr.id: ( 1 + random.random() * (bidding_factor_max - 1) ) for slr in seller_list}  # range [1, bidding_factor_max]
        self.bidding_factor_increase = 0.5 #range_bidding_factor_increase[0] + random.random() * (range_bidding_factor_increase[1] - range_bidding_factor_increase[0])  # random number between min_bidding_factor_increase and bidding_factor_max
        self.bidding_factor_decrease = 0.5 #range_bidding_factor_decrease[0] + random.random() * (range_bidding_factor_decrease[1] - range_bidding_factor_decrease[0])  # random number between 0 and 1

    def get_bidding_factor(self, seller_id):
        return self.bidding_factor_list[seller_id]


    def make_the_bid(self, seller_id, starting_price):
        return self.bidding_factor_list[seller_id] * starting_price


    def add_to_profit(self, profit):
        self.profit += profit

    def uniform_closed(self, a, b):
        while True:
            r = random.uniform(a, b)  # range [a, b)
            if r > a: return r  # range (a, b)

    def increase_bid_factor(self, seller_id):
        self.bidding_factor_list[seller_id] += self.uniform_closed(0, 1)
        if self.bidding_factor_list[seller_id] < 1:
            self.bidding_factor_list[seller_id] = 1
        #elif self.bidding_factor_list[seller_id] > self.bidding_factor_max:
        #    self.bidding_factor_list[seller_id] = self.bidding_factor_max



    def decrease_bid_factor(self, seller_id):
        self.bidding_factor_list[seller_id] -= self.uniform_closed(0, 1)
        if self.bidding_factor_list[seller_id] < 1:
            self.bidding_factor_list[seller_id] = 1
        #elif self.bidding_factor_list[seller_id] > self.bidding_factor_max:
        #    self.bidding_factor_list[seller_id] = self.bidding_factor_max
