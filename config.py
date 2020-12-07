
SEED = 1

ROUNDS = 1000

test_list = [
    {
        "id": "1",
        "execute": True,
        "times": 10,
        "n_buyers": 3,
        "n_sellers": 2,
        "n_rounds": ROUNDS,
        "max_starting_price": 10,
        "max_bidding_factor": 5,
        "epsilon": 0.1,
        "type": "PURE_AUCTIONING",
        "params": {
            "BIDDING_STRATEGY": [],
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
