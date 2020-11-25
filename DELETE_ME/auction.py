import statistics
from collections import OrderedDict
from random import random

from auction_type import AuctionType
from bid_history_entry import BidHistoryEntry


class Auction:

    def __init__(self, s_max, seller, buyers, round_bid_history, epsilon, type):
        self.s_k = random() * s_max
        self.seller = seller
        self.buyers = buyers
        self.bids = {}
        self.round_bid_history = round_bid_history
        self.epsilon = epsilon
        self.type = type

    def run(self):
        for buyer in self.buyers:
            bid = buyer.bidding_factors[self.seller.id] * self.s_k
            history_entry = self.round_bid_history.get(buyer)

            #check if the buyer already won a previous auction in the round
            if history_entry is not None:
                bid -= ((history_entry.market_price - history_entry.price) + self.epsilon * history_entry.price)
                if(bid < 0):
                    bid = 0

            self.bids[buyer] = bid

        # calculate market price
        market_price = statistics.mean(self.bids.values())

        previous_buyer = None
        winner = None
        #sort dictionary by values
        sorted_bids = OrderedDict(sorted(self.bids.items(), key=lambda item: item[1]))

        #find winner and price
        for buyer, bid in sorted_bids.items():
            if bid > market_price:
                break
            previous_buyer = winner
            winner = buyer

        price = 0.00
        if previous_buyer is not None:
            price = self.bids[previous_buyer]
        else:
            price = (self.bids[winner] + self.s_k) / 2

        #add profits
        self.seller.add_to_profit(price)
        self.seller.add_to_market_prices(market_price)
        buyer_profit = market_price - price
        winner.add_to_profit(buyer_profit)
        history_entry = self.round_bid_history.get(winner)

        #if the auction type is leveled commitment, a history entry must be added
        create_history_entry = self.type == AuctionType.LEVELED_COMMITMENT

        #check if the buyer already won a previous auction in the round
        if history_entry is not None:
            previous_seller = history_entry.seller
            previous_market_price = history_entry.market_price
            previous_price = history_entry.price
            previous_buyer_profit = previous_market_price - previous_price
            previous_penalty_fee = self.epsilon * previous_price
            penalty_fee = self.epsilon * price
            #check if the new profit is higher than the previous profit
            if previous_buyer_profit - previous_penalty_fee < buyer_profit - penalty_fee:
                #remove previous profits and add annulling penalty fee
                previous_seller.add_to_profit(-previous_price)
                previous_seller.add_to_profit(previous_penalty_fee)
                winner.add_to_profit(-previous_buyer_profit)
                winner.add_to_profit(-previous_penalty_fee)
            else:
                #remove current profits and add annulling penalty fee
                self.seller.add_to_profit(-price)
                self.seller.add_to_profit(penalty_fee)
                winner.add_to_profit(-buyer_profit)
                winner.add_to_profit(-penalty_fee)
                #the current profits must not be added in the history
                create_history_entry = False

        if create_history_entry:
            #create or overwrite previous history entries
            self.round_bid_history[winner] = BidHistoryEntry(self.seller, market_price, price)

        #increase/decrease bid factors
        for buyer, bid in sorted_bids.items():
            if buyer == winner or bid >= market_price:
                buyer.decrease_bid_factor(self.seller.id)
            else:
                buyer.increase_bid_factor(self.seller.id)

        return winner