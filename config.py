
SEED = 1

ROUNDS = 1000



test_list = [
    {
        "id": "1",
        "execute": True,
        "times": 10,
        "n_buyers": 4,
        "n_sellers": 3,
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
    },
    {
        "id": "2",
        "execute": False,
        "times" : 100,
        "n_buyers": 5,
        "n_sellers": 10,
        "n_rounds": ROUNDS,
        "max_starting_price": 10,
        "max_bidding_factor": 66,
        "epsilon": 1,
        "type": "PURE_AUCTIONING",
        "params": {}
    }
]
