import config as cfg
import matplotlib.pyplot as plt
import numpy as np
# from numpy import random
import matplotlib.pyplot as plt
import time
import pandas as pd
import seller
import buyer
import random

from copy import deepcopy

np.random.seed(1)
# print(np.random.permutation(10))


def plot_graph_result(test_name, epoch_list, avg_list, max_list, min_list, show=False):
    plt.plot(epoch_list, avg_list, label="avg", color="green")
    plt.plot(epoch_list, max_list, label="max", color="red")
    plt.plot(epoch_list, min_list, label="min", color="blue")
    plt.legend(loc='upper left')

    date = time.strftime("%Y_%m_%d_%H_%M_%S")
    plt.savefig(f"imgs\\graph_test_{test_name}_{date}")

    if show:
        plt.show()

    plt.clf()


def plot_heat_map(test_name, q_table, show=False):
    heatmap = np.max(q_table, axis=2)
    plt.imshow(heatmap, cmap='jet', interpolation='nearest', extent=[-0.07, 0.07, 0.6, -1.2], aspect='auto')
    plt.title("State Value function")
    plt.xlabel("Speed (-0.07 to 0.07)")
    plt.ylabel("Position (-1.2 to 0.6)")
    plt.gca().invert_yaxis()
    plt.colorbar()

    date = time.strftime("%Y_%m_%d_%H_%M_%S")
    plt.savefig(f"imgs\\heatmap_test_{test_name}_{date}")

    if show:
        plt.show()

    plt.clf()


def launch_new_test(id, n_buyers, n_sellers, n_rounds, max_starting_price, max_bidding_factor, epsilon, type, params={}):
    if n_sellers >= n_buyers:
        print("ERROR: (", id,") Buyers have to be more than Sellers")
        return None

    biddin_strategy_data, seller_strategy_data = None, None
    if params:
        biddin_strategy_data = params.get('BIDDING_STRATEGY')
        seller_strategy_data = params.get('SELLER_STRATEGY')


    # init OUTCOME
    outcome = []

    market_price_list, seller_profit_list, buyer_profit_list = [], [], []

    # init AGENTS
    seller_list = [seller.Seller(i) for i in range(n_sellers)]
    buyer_list = [buyer.Buyer(i, seller_list, max_bidding_factor) for i in range(n_buyers)]


    if type == "PURE_AUCTIONING":
        for round in range(n_rounds):
            # for every round init this dict and added the lists of data during the auctions
            round_stats = {
                "id": round,
                "market_price": [],
                "seller_profit": [],
                "buyer_profit": []
            }

            # created a shuffled copy of the buyer_list and seller_list every round
            sellers = random.sample(seller_list, len(seller_list))
            buyers  = random.sample(buyer_list, len(buyer_list))

            # start the auctions
            for slr in sellers:
                seller_price = slr.init_random_starting_price(max_starting_price)

                # the buyers start the bids
                bid_list = []
                for bur in buyers:
                    # make the bid thanks to the factor given by the factor list
                    buyer_bid = bur.get_bidding_factor(slr.id) * seller_price
                    bid_list.append(buyer_bid)  # note: this bids have the same order of buyer_turn_list

                # bid end
                market_price = sum(bid_list) / len(bid_list)  # avg of all the bids

                bid_list = [(bid if bid <= market_price else 0) for bid in bid_list]  # remove the values over the market_price
                winner_index = bid_list.index(max(bid_list))  # found the first winner, the other ones... NO
                bid_list[winner_index] = 0   # removed is offer...
                winner_payment = np.amax(bid_list)  # ...to pick the second max

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

                round_stats["market_price"].append(market_price)
                round_stats["seller_profit"].append(seller_profit)
                round_stats["buyer_profit"].append(winner_profit)

                if biddin_strategy_data:
                    for b in bid_list:
                        if b == 0:
                            buyer_list[bid_list.index(b)].decrease_bid_factor(slr.id)
                        else:
                            buyer_list[bid_list.index(b)].increase_bid_factor(slr.id)
                elif seller_strategy_data:
                    pass

            outcome.append(round_stats)

    elif type == "LEVELED_COMMITMENT_AUCTIONING":
        for round in range(n_rounds):
            buyers_won_auction = {}
            # created a shuffled copy of the buyer_list and seller_list every round
            sellers = random.sample(seller_list, len(seller_list))
            buyers  = random.sample(buyer_list, len(buyer_list))

            # start the auctions
            for slr in sellers:
                seller_price = slr.init_random_starting_price(max_starting_price)

                # the buyers start the bids
                bid_list = []
                for bur in buyers:
                    # make the bid thanks to the factor given by the factor list
                    buyer_bid = bur.get_bidding_factor(slr.id) * seller_price
                    bid_list.append(buyer_bid)  # note: this bids have the same order of buyer_turn_list

                # bid end
                market_price = sum(bid_list) / len(bid_list)  # avg of all the bids

                bid_list = [(bid if bid <= market_price else 0) for bid in bid_list]  # remove the values over the market_price
                winner_index = bid_list.index(max(bid_list))  # found the first winner, the other ones... NO
                bid_list[winner_index] = 0  # removed is offer...
                winner_payment = np.amax(bid_list)  # ...to pick the second max

                # profit for sellers
                seller_profit = winner_payment - seller_price

                # profit for buyers
                winner = buyers.__getitem__(winner_index)  # remove the winner from the other auctions
                print("winner,", winner.id)
                winner_profit = market_price - winner_payment
                # add the buyer id inside the dict, if the key already exists, it return the previous value
                prev_auction = buyers_won_auction.setdefault(winner.id, (slr.id, winner_payment, winner_profit))
                penalty_fee = 0
                print("both id", prev_auction[0], slr.id)
                if prev_auction[0] != slr.id:
                    print("id", winner.id, "won more than 1 auction, prv:", prev_auction[0], "new", slr.id)
                    if winner_profit > prev_auction[2]:
                        print("new profit is more than before")
                        penalty_fee = epsilon * prev_auction[1]
                        print(buyers_won_auction[winner.id])
                        buyers_won_auction[winner.id] = (slr.id, winner_payment, winner_profit)
                        print("after update", buyers_won_auction[winner.id])

                    else:
                        print("new profit is less than before")
                        penalty_fee = epsilon * winner_payment

                for real_slr in seller_list:  # update the seller profit, Note: the real list
                    if real_slr.id == slr.id:
                        real_slr.add_to_profit(seller_profit)
                    if real_slr.id == prev_auction[0]:
                        print("fee", penalty_fee)
                        real_slr.add_to_profit(penalty_fee)

                for real_bur in buyer_list:  # update the buyer profit, Note: the real list
                    if real_bur.id == winner.id:
                        real_bur.add_to_profit(winner_profit)
                    if real_bur.id == prev_auction[0]:
                        real_bur.add_to_profit(-penalty_fee)

                market_price_list.append(market_price)
                seller_profit_list.append(seller_profit)
                buyer_profit_list.append(winner_profit)

    return outcome


def main():

    for test in cfg.test_list:

        if test["execute"]:  # add this because we could want save tests on config but not test them sometimes
            result_list = []
            for n in range(test["times"]):
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
            else:
                result_list.append(result)

            asd = 1





        # TODO here all the graphs and tables

if __name__ == "__main__":
    main()
