SEED = 1

ROUNDS = 1000
TIMES = 10

SHOW_PRINT = False
SHOW_SINGLE_GRAPH = False
SHOW_MULTI_GRAPH = True
STEP_PLOTTING = None
# LEVELED_COMMITMENT_AUCTIONING
# PURE_AUCTIONING

TEST_TITLE = "Variation Bidding Factor Decrease (Leveled Commitment)"
TYPE = "LEVELED_COMMITMENT_AUCTIONING"

test_list = [
    {
        "id": "Bid Factor Decrease 02-04",
        "execute": True,
        "times": TIMES,
        "n_buyers": 4,
        "n_sellers": 3,
        "n_rounds": ROUNDS,
        "max_starting_price": 10,
        "range_bidding_factor_increase": [1, 2],
        "range_bidding_factor_decrease": [0.2, 0.4],
        "max_bidding_factor": 2,
        "epsilon": 0.2,
        "type": TYPE,
        "params": {
            "BIDDING_STRATEGY": True,
            "SELLER_STRATEGY": None
        }
    },
    {
        "id": "Bid Factor Decrease 04-06",
        "execute": True,
        "times": TIMES,
        "n_buyers": 4,
        "n_sellers": 3,
        "n_rounds": ROUNDS,
        "max_starting_price": 10,
        "range_bidding_factor_increase": [1, 2],
        "range_bidding_factor_decrease": [0.4, 0.6],
        "max_bidding_factor": 2,
        "epsilon": 0.2,
        "type": TYPE,
        "params": {
            "BIDDING_STRATEGY": True,
            "SELLER_STRATEGY": None
        }
    },
    {
        "id": "Bid Factor Decrease 06-08",
        "execute": True,
        "times": TIMES,
        "n_buyers": 4,
        "n_sellers": 3,
        "n_rounds": ROUNDS,
        "max_starting_price": 10,
        "range_bidding_factor_increase": [1, 2],
        "range_bidding_factor_decrease": [0.6, 0.8],
        "max_bidding_factor": 2,
        "epsilon": 0.2,
        "type": TYPE,
        "params": {
            "BIDDING_STRATEGY": True,
            "SELLER_STRATEGY": None
        }
    },
    {
        "id": "Bid Factor Decrease 08-10",
        "execute": True,
        "times": TIMES,
        "n_buyers": 4,
        "n_sellers": 3,
        "n_rounds": ROUNDS,
        "max_starting_price": 10,
        "range_bidding_factor_increase": [1, 2],
        "range_bidding_factor_decrease": [0.8, 1],
        "max_bidding_factor": 2,
        "epsilon": 0.2,
        "type": TYPE,
        "params": {
            "BIDDING_STRATEGY": True,
            "SELLER_STRATEGY": None
        }
    }
]

"""
for buyer in range(1, 5):
    if buyer < 1:
        continue
    for seller in range(1, 5):
        if seller >= buyer:
            continue
        print(seller, buyer)
        test_list.append(
            {
                "id": f"buyer:{buyer}, seller:{seller}",
                "execute": True,
                "times": 10,
                "n_buyers": buyer,
                "n_sellers": seller,
                "n_rounds": ROUNDS,
                "max_starting_price": 10,
                "range_bidding_factor_increase": [1, 10],
                "range_bidding_factor_decrease": [0, 1],
                "max_bidding_factor": 10,
                "epsilon": 0.2,
                "type": "PURE_AUCTIONING",
                "params": {
                    "BIDDING_STRATEGY": True,
                    "SELLER_STRATEGY": None
                },
            }

        )
"""
