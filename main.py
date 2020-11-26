import config as cfg
import matplotlib.pyplot as plt
import numpy
from numpy import random
import pandas as pd
import seller
import buyer

numpy.random.seed(1)
print(random.permutation(10))



def launch_new_test(id, n_buyers, n_sellers, n_rounds, max_starting_price, epsilon, type, params = []):
    if n_sellers >= n_buyers:
        print("ERROR: Buyers have to be more than Sellers")
        return None

    # init OUTCOME
    market_price_stats, seller_profit, buyer_profit = 1, 1, 1

    # init AGENTS
    seller_list = [seller.Seller(i) for i in range(n_sellers)]
    buyer_list  = [buyer.Buyer(i, n_sellers, 666) for i in range(n_buyers)]



    for round in range(n_rounds):
        seller_turn_list = random.permutation(n_sellers) # every round the seller order is random
        buyer_turn_list = random.permutation(n_buyers)  # every round the buyers order is random

        for t_s in seller_turn_list:
            seller_offer = seller_list[t_s].init_random_starting_price(max_starting_price)

            bid_list = []
            for t_b in buyer_turn_list:
                buyer_bid = buyer_list[t_b].bidding_factor_list[t_s] # make the bid thanks to the factor given by the factor list
                bid_list.append(buyer_bid)

            market_price = sum(bid_list)/len(bid_list) # avg of all the bids

            bid_list = [ (bid if bid <= market_price else 0) for bid in bid_list] # remove the values over the market_price
            winner_index = numpy.where(bid_list == numpy.amax(bid_list)) # found the winner
            bid_list[int(winner_index[0])] = 0 # remove is offer
            winner_spent = numpy.amax(bid_list) # to pick the second max

            # TODO maybe the real index is in buyer_turn_list CHECK

    return market_price_stats, seller_profit, buyer_profit


def main():
    for test in cfg.test_list:
        if test["execute"]:  # add this because we could want save tests on config but not test them sometimes
            result = launch_new_test(
                test["id"],
                test["n_buyers"],
                test["n_sellers"],
                test["n_rounds"],
                test["max_starting_price"],
                test["epsilon"],
                test["type"],
                test["params"]
            )
            if not result:
                return 1



if __name__ == "__main__":
    main()
