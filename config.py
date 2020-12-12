SEED = 2

ROUNDS = 1000
TIMES = 10

SHOW_PRINT = False
SHOW_SINGLE_GRAPH = False
SHOW_MULTI_GRAPH = True
STEP_PLOTTING = None
# LEVELED_COMMITMENT_AUCTIONING
# PURE_AUCTIONING

TEST_TITLE = "Confront Auctioning Types"
TYPE = "LEVELED_COMMITMENT_AUCTIONING"

test_list = [
    {
        "id": "pure",
        "execute": True,
        "times": TIMES,
        "n_buyers": 2,
        "n_sellers": 1,
        "n_rounds": ROUNDS,
        "max_starting_price": 10,
        "range_bidding_factor_increase": [1, 2],
        "range_bidding_factor_decrease": [0, 1],
        "max_bidding_factor": 2,
        "epsilon": 0.2,
        "type": "PURE_AUCTIONING",
        "params": {
            "BIDDING_STRATEGY": True,
            "SELLER_STRATEGY": None
        }
    },
    {
        "id": "leveled commitment",
        "execute": True,
        "times": TIMES,
        "n_buyers": 2,
        "n_sellers": 1,
        "n_rounds": ROUNDS,
        "max_starting_price": 10,
        "range_bidding_factor_increase": [1, 2],
        "range_bidding_factor_decrease": [0, 1],
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
