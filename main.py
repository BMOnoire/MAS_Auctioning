import config as cfg
import matplotlib.pyplot as plt
import numpy as np
#from numpy import random
import pandas as pd
import seller
import buyer
import random

np.random.seed(1)
print(np.random.permutation(10))



def launch_new_test(id, n_buyers, n_sellers, n_rounds, max_starting_price, max_bidding_factor, epsilon, type, params = []):
    if n_sellers >= n_buyers:
        print("ERROR: Buyers have to be more than Sellers")
        return None

    # init OUTCOME
    market_price_list, seller_profit_list, buyer_profit_list = [], [], []

    if type == "PURE_AUCTIONING":

        # init AGENTS
        seller_list = [seller.Seller(i) for i in range(n_sellers)]
        buyer_list  = [buyer.Buyer(i, seller_list, max_bidding_factor) for i in range(n_buyers)]


        for round in range(n_rounds):
            # created a shuffled copy of the buyer_list and seller_list every round
            sellers = random.sample(seller_list, len(seller_list))
            buyers  = random.sample(buyer_list, len(buyer_list))


            # start the auctions
            for slr in sellers:

                seller_price = slr.init_random_starting_price(max_starting_price)


                # the buyers start the bids
                bid_list = []
                for bur in buyers:
                    buyer_bid = bur.get_bidding_factor(slr.id) * seller_price  # make the bid thanks to the factor given by the factor list

                    bid_list.append(buyer_bid) # note: this bids have the same order of buyer_turn_list

                # bid end
                market_price = sum(bid_list)/len(bid_list) # avg of all the bids

                bid_list = [ (bid if bid <= market_price else 0) for bid in bid_list]  # remove the values over the market_price
                winner_index = bid_list.index(max(bid_list)) # found the first winner, the other ones... NO
                bid_list[winner_index] = 0 # removed is offer...
                winner_payment = np.amax(bid_list) # ...to pick the second max

                # profit for sellers
                seller_profit = winner_payment - seller_price
                for real_slr in seller_list:  # update the seller profit, Note: the real list
                    if real_slr.id == slr.id:
                        real_slr.add_to_profit(seller_profit)


                # profit for buyers
                winner = buyers.pop(winner_index)  # remove the winner from the other auctions
                winner_profit = market_price - winner_payment

                for real_bur in buyer_list:  # update the buyer profit, Note: the real list
                    if real_bur.id == winner.id:
                        real_bur.add_to_profit(winner_profit)

                market_price_list.append(market_price)
                seller_profit_list.append(seller_profit)
                buyer_profit_list.append(winner_profit)




    return market_price_list, seller_profit_list, buyer_profit_list


def main():
    for test in cfg.test_list:
        if test["execute"]:  # add this because we could want save tests on config but not test them sometimes
            result = launch_new_test(
                test["id"],
                test["n_buyers"],
                test["n_sellers"],
                test["n_rounds"],
                test["max_starting_price"],
                test["max_bidding_factor"],
                test["epsilon"],
                test["type"],
                test["params"]
            )
            if not result:
                return 1



if __name__ == "__main__":
    main()
