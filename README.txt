There are no libraries needed to launch the project

To launch the simulator use main.py

If you want to change the behaviour of the program then modify the file config.py
	
	############  CONFIG ################# 
	
	some tips:

		TIMES: 			decide the number of simulation to perform the average
		SHOW_MULTI_GRAPH:   	allows the simulator to plot an image with market price, seller profit and buyer profit comparisons.
		max_bidding_factor: 	define the maximum value for the bidding factor. Bidding factor are then initialized between a range of 0 and max_bidding_factor
		SELLER_STRATEGY: 	decide which type of strategy try for the seller, accepted parameters are None, "OWN", "COM"