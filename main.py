import config as cfg
import matplotlib.pyplot as plt
import numpy
import pandas as pd
import seller
import buyer



def launch_new_test(id, n_buyers, n_sellers, n_rounds, max_starting_price, epsilon, type, params = []):
    if n_sellers >= n_buyers:
        print("ERROR: Buyers have to be more than Sellers")
        return None

    # init OUTCOME
    market_price_stats, seller_profit, buyer_profit = 1, 1, 1

    # init AGENTS
    seller_list = [seller.Seller(i) for i in range(n_sellers)]
    buyer_list  = [buyer.Buyer(i,n_sellers, 666) for i in range(n_buyers)]



    # todo all the stuff for one test


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
