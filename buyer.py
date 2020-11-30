from random import random


class Buyer:

    def __init__(self, id, seller_list, bidding_factor_max):
        self.id = id
        self.profit = 0.0
        self.bidding_factor_max = bidding_factor_max
        self.bidding_factor_list = { slr.id: ( 1 + random() * (bidding_factor_max - 1) ) for slr in seller_list}  # range [1, bidding_factor_max]


    def get_bidding_factor(self, seller_id):
        return self.bidding_factor_list[seller_id]


    def add_to_profit(self, profit):
        self.profit += profit


    def increase_bid_factor(self, seller_id):
        self.bidding_factors[seller_id] += random() * (self.bidding_factor_max - self.bidding_factors[seller_id])


    def decrease_bid_factor(self, seller_id):
        self.bidding_factors[seller_id] -= random() * (self.bidding_factors[seller_id] - 1)
