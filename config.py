
test_list = [
    {
        "id": "first_try",
        "execute": True,
        "times": 1,
        "n_buyers": 8,
        "n_sellers": 7,
        "n_rounds": 9,
        "max_starting_price": 10,
        "max_bidding_factor": 66,
        "epsilon": 0.1,
        "type": "PURE_AUCTIONING",
        "params": {
            "BIDDING_STRATEGY": [],
            "SELLER_STRATEGY": None
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
