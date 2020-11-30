
test_list = [
    {
        "id": "first_try",
        "execute": True,
        "times": 2,
        "n_buyers": 8,
        "n_sellers": 7,
        "n_rounds": 9,
        "max_starting_price": 10,
        "max_bidding_factor": 66,
        "epsilon": 0.1,
        "type": "LEVELED_COMMITMENT",
        "params": {
            "BIDDING_STRATEGY": 1,
            "SELLER_STRATEGY": "TODO_something"
        }
    },
    {
        "id": "first_nope",
        "execute": False,
        "times" : 2,
        "n_buyers": 6,
        "n_sellers": 7,
        "n_rounds": 8,
        "max_starting_price": 10,
        "max_bidding_factor": 66,
        "epsilon": 1,
        "type": "PURE_AUCTIONING",
        "params": {}
    }
]
