from random import random


class Buyer:
    def __init__(self, id, number_sellers, bidding_factor_max):
        self.id = id
        self.profit = 0.0
        self.bidding_factors = []
        self.bidding_factor_max = bidding_factor_max
        for i in range(number_sellers):
            self.bidding_factors.append(1 + random() * (bidding_factor_max - 1))

    def decrease_bid_factor(self, seller_id):
        self.bidding_factors[seller_id] -= random() * (self.bidding_factors[seller_id] - 1)

    def increase_bid_factor(self, seller_id):
        self.bidding_factors[seller_id] += random() * (self.bidding_factor_max - self.bidding_factors[seller_id]);

    def add_to_profit(self, profit):
        self.profit += profit
