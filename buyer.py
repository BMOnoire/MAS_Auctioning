from random import random


class Buyer:

    def __init__(self, id, n_sellers, bidding_factor_max):
        self.id = id
        self.profit = 0.0
        self.bidding_factor_max = bidding_factor_max
        self.bidding_factor_list = [1 + random() * (bidding_factor_max - 1) for _ in range(n_sellers)]  # range [1, bidding_factor_max]


    def decrease_bid_factor(self, seller_id):
        self.bidding_factors[seller_id] -= random() * (self.bidding_factors[seller_id] - 1)

    def increase_bid_factor(self, seller_id):
        self.bidding_factors[seller_id] += random() * (self.bidding_factor_max - self.bidding_factors[seller_id]);

    def add_to_profit(self, profit):
        self.profit += profit
