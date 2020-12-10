import numpy as np
import seller
import buyer
import random
import statistics as stats
import janitor
import config as cfg
import plotting

if cfg.SEED:
    random.seed(cfg.SEED)


def launch_new_test(id, n_buyers, n_sellers, n_rounds, max_starting_price, max_bidding_factor, range_bidding_factor_increase, range_bidding_factor_decrease, epsilon, type, params={}):
    if n_sellers >= n_buyers:
        print("ERROR: (", id,") Buyers have to be more than Sellers, change it")
        return None

    if type != "LEVELED_COMMITMENT_AUCTIONING" and type != "PURE_AUCTIONING":
        print("ERROR: (", id,") wrong auctioning type, change it")
        return None

    bidding_strategy_data, seller_strategy_data = None, None
    if params:
        bidding_strategy_data = params.get('BIDDING_STRATEGY')
        seller_strategy_data = params.get('SELLER_STRATEGY')
        if seller_strategy_data and seller_strategy_data != "OWN" and seller_strategy_data != "COM": # no right params
            print("ERROR: (", id, ") seller strategy with wrong params, change it")
            return None

    # init OUTCOME
    outcome = []

    # init AGENTS
    seller_list = [seller.Seller(i, seller_strategy_data) for i in range(n_sellers)]
    buyer_list = [buyer.Buyer(i, seller_list, max_bidding_factor, range_bidding_factor_increase, range_bidding_factor_decrease) for i in range(n_buyers)]


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
        buyers = random.sample(buyer_list, len(buyer_list))

        buyers_won_auction = {}  # only for leveled

        # start the auctions
        for current_seller in sellers:
            seller_price = current_seller.init_random_starting_price(max_starting_price)
            print("seller_price", seller_price)

            # the buyers start the bids
            # make the bid thanks to the factor given by the factor list
            # note: this bids have the same order of buyer_turn_list
            bid_list = [buyer.make_the_bid(current_seller.id, seller_price) for buyer in buyers]
            # bid end

            # MARKET PRICE
            market_price = sum(bid_list) / len(bid_list)  # avg of all the bids
            round_stats["market_price"].append(market_price)
            print("market_price", market_price)

            # FIND THE WINNER
            bid_list = [(bid if bid <= market_price else 0) for bid in bid_list]  # remove the values over the market_price

            first_best_bid = max(bid_list)
            winner_index = bid_list.index(first_best_bid)  # found the first winner, the other ones... NO

            bid_list[winner_index] = 0  # removed is offer (best_bid)...
            second_best_bid = max(bid_list)  # ...to pick the second max

            if not second_best_bid:  # there is only one winner and the max is 0
                second_best_bid = 0.5 * (first_best_bid + seller_price)

            print("payment price", second_best_bid)
            # profit for sellers
            seller_profit = second_best_bid - seller_price

            # profit for buyers
            winner_profit = market_price - second_best_bid

            print("profit (winner, seller)", winner_profit, seller_profit)

            if bidding_strategy_data:
                for i in range(len(bid_list)):
                    if bid_list[i] == 0:
                        buyer_list[buyers[i].id].decrease_bid_factor(current_seller.id)
                    else:
                        buyer_list[buyers[i].id].increase_bid_factor(current_seller.id)

            bid_factor_list = [buyer.bidding_factor_list[current_seller.id] for buyer in buyers]
            # print("bid_factor_list", bid_factor_list)
            bid_factor_list2 = [buyer.bidding_factor_list[current_seller.id] for buyer in buyer_list]
            # print("bid_factor_list2", bid_factor_list2)

            if type == "PURE_AUCTIONING":

                # remove the winner from the other auctions
                winner = buyers.pop(winner_index)

            elif type == "LEVELED_COMMITMENT_AUCTIONING":

                # get the winner from the other auctions
                winner = buyers.__getitem__(winner_index)

                current_auction = (current_seller.id, second_best_bid, winner_profit)

                # check if there is previous bidding for the winner id
                previous_auction = buyers_won_auction.get(winner.id)

                if previous_auction:  # if there is a previous win

                    if winner_profit > previous_auction[2]:  # if the current profit is better than the previous, decommit previous bid and save the new one
                        buyers_won_auction[winner.id] = current_auction  # update the last bid

                        penalty_fee = epsilon * previous_auction[1]
                        # refund the previous seller price minus the penalty fee
                        refund_seller_index = previous_auction[0]

                    else: # decommit current bid
                        penalty_fee = epsilon * current_auction[1]
                        # refund the current seller price minus the penalty fee
                        refund_seller_index = current_seller.id

                    # refund seller loop
                    for real_seller in seller_list:
                        if real_seller.id == refund_seller_index:
                            real_seller.add_to_profit(penalty_fee)
                            break

                    # refund buyer loop
                    for real_buyer in buyer_list:
                        if real_buyer.id == winner.id:
                            real_buyer.add_to_profit(-penalty_fee)
                            break

                else: # else save the current one
                    buyers_won_auction[winner.id] = current_auction

            # update the seller profit, Note: the real list
            for real_seller in seller_list:
                if real_seller.id == current_seller.id:
                    real_seller.add_to_profit(seller_profit)
                    break

            # update the buyer profit, Note: the real list
            for real_buyer in buyer_list:
                if real_buyer.id == winner.id:
                    real_buyer.add_to_profit(winner_profit)
                    break

            profit_buyer = [buyer.profit for buyer in buyer_list]
            profit_seller = [seller.profit for seller in seller_list]
            print("seller_profit", profit_seller)
            print("buyer_profit", profit_buyer)

            if seller_strategy_data:
                pass

        round_stats["seller_profit"] = [seller.profit for seller in seller_list]
        round_stats["buyer_profit"] = [buyer.profit for buyer in buyer_list]

        outcome.append(round_stats)

    return outcome


def main():
    id_list, market_list, seller_list, buyer_list = [], [], [], []

    for test in cfg.test_list:

        if not test["execute"]:  # add this because we could want save tests on config but not test them sometimes
            continue

        result_list = []
        for n in range(test["times"]):
            result = launch_new_test(
                test["id"],
                test["n_buyers"],
                test["n_sellers"],
                test["n_rounds"],
                test["max_starting_price"],
                test["max_bidding_factor"],
                test["range_bidding_factor_increase"],
                test["range_bidding_factor_decrease"],
                test["epsilon"],
                test["type"],
                test["params"]
            )
            if not result:

                return 1
            else:
                result_list.append(result)

        round_list = range(test["n_rounds"])
        market_final_value, seller_final_value, buyer_final_value = [0] * test["n_rounds"], [0] * test["n_rounds"], [0] * test["n_rounds"]
        for result in result_list:
            avg_market_price_list, avg_seller_profit_list, avg_buyer_profit_list = [], [], []
            for round in result:
                avg_market_price = stats.mean(round["market_price"])
                avg_seller_profit = stats.mean(round["seller_profit"])
                avg_buyer_profit = stats.mean(round["buyer_profit"])

                avg_market_price_list.append(avg_market_price)
                avg_seller_profit_list.append(avg_seller_profit)
                avg_buyer_profit_list.append(avg_buyer_profit)

            market_final_value = [a + b for a, b in zip(market_final_value, avg_market_price_list)]
            seller_final_value = [a + b for a, b in zip(seller_final_value, avg_seller_profit_list)]
            buyer_final_value  = [a + b for a, b in zip(buyer_final_value, avg_buyer_profit_list)]

        market_final_value = np.array(market_final_value) / test["times"]
        seller_final_value = np.array(seller_final_value) / test["times"]
        buyer_final_value  =  np.array(buyer_final_value) / test["times"]


        plotting.plot_graph_result(test["id"], "market_price", round_list, market_final_value, cfg.STEP_PLOTTING, cfg.SHOW_SINGLE_GRAPH)
        plotting.plot_graph_result(test["id"], "seller_profit", round_list, seller_final_value, cfg.STEP_PLOTTING, cfg.SHOW_SINGLE_GRAPH)
        plotting.plot_graph_result(test["id"], "buyer_profit", round_list, buyer_final_value, cfg.STEP_PLOTTING, cfg.SHOW_SINGLE_GRAPH)

        plotting.plot_value_comparison(test["id"], round_list, market_final_value, seller_final_value, buyer_final_value, cfg.STEP_PLOTTING, cfg.SHOW_MULTI_GRAPH)

        id_list.append(test["id"]),
        market_list.append(market_final_value)
        seller_list.append(seller_final_value)
        buyer_list.append(buyer_final_value)


    plotting.plot_diff_results("test_comparison", round_list, id_list, market_list, seller_list, buyer_list, cfg.STEP_PLOTTING, cfg.SHOW_MULTI_GRAPH)

if __name__ == "__main__":
    janitor.create_dir("imgs")
    main()
