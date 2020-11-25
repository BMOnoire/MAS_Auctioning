import random
import statistics

from auction import Auction
from auction_type import AuctionType
from buyer import Buyer
from seller import Seller


class Simulation:

    def __init__(self, k, n, r, s_max, epsilon, type, bidding_factor_max):
        if n <= k:
            raise Exception("The number of buyers has to be greater than the number of sellers")

        self.sellers = []
        for i in range(k):
            self.sellers.append(Seller(i))

        self.buyers = []
        for i in range(n):
            self.buyers.append(Buyer(i, k, bidding_factor_max));

        self.r = r
        self.s_max = s_max
        self.epsilon = epsilon
        self.type = type
        self.buyer_profits_average = 0.0
        self.seller_profits_average = 0.0

    def run(self):
        for round in range(self.r):
            buyers = self.buyers.copy()
            random.shuffle(self.sellers)
            round_bid_history = {}
            for seller in self.sellers:
                auction = Auction(self.s_max, seller, buyers, round_bid_history, self.epsilon, self.type)
                winner = auction.run()
                if self.type == AuctionType.PURE:
                    buyers.remove(winner)

        self.sellers.sort(key=lambda x: x.id)

        self.seller_profits_average = statistics.mean([seller.profit for seller in self.sellers])

        self.buyer_profits_average = statistics.mean([buyer.profit for buyer in self.buyers])


