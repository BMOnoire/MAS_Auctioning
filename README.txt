To launch the project just install:

	pip install matplotlib
	pip install numpy

To launch the simulator use main.py

If you want to change the behaviour of the program then modify the file config.py
	
	
	############  CONFIG ################# 
	
	global parameters tips:

		ROUNDS: 			the number of rounds of the simulation 
		TIMES: 				decide the number of simulation to perform the average
		SHOW_SINGLE_GRAPH:	show all the graphs for every test
		SHOW_MULTI_GRAPH:   allows the simulator to plot an image with market price, seller profit and buyer profit comparisons.
		STEP_PLOTTING:		set None to show all the results of every round, otherwise the result of every N number 
		
		
	test list tips:
		test_list = [
		
			{
				"id": "PURE",     
				"execute": False,       <---------------------- if false you can skip this test
				"times": TIMES,
				"n_buyers": 10,
				"n_sellers": 7,
				"n_rounds": ROUNDS,
				"max_starting_price": 10,      <-------------- define the maximum value for the starting price. It is initialized between a range of 0 and max_starting_price
				"range_bidding_factor_increase": [1, 2],    <- random init between this range
				"range_bidding_factor_decrease": [0.5, 1],  <- random init between this range
				"max_bidding_factor": 2,       <-------------- define the maximum value for the bidding factor. It is initialized between a range of 0 and max_bidding_factor
				"epsilon": 0.2,
				"type": "PURE_AUCTIONING",
				"params": {
					"BIDDING_STRATEGY": True,  <------- True or False
					"SELLER_STRATEGY": None    <------- decide which type of strategy try for the seller, accepted parameters are None, "OWN", "COM"
				}, 
			},
			
			....
		]