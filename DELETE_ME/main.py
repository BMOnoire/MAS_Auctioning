import matplotlib.pyplot as plt
import numpy
import pandas as pd

from auction_type import AuctionType
from simulation import Simulation

def create_output(experiment_name ,file_name, epsilons, pure_buyer_profits_average, pure_seller_profits_average, leveled_commitment_buyer_profits_average, leveled_commitment_seller_profits_average):
    df = pd.DataFrame()
    df[experiment_name] = epsilons
    df['Pure buyer profits'] = pure_buyer_profits_average
    df['Pure seller profits'] = pure_seller_profits_average
    df['Leveled commitment buyer profits'] = leveled_commitment_buyer_profits_average
    df['Leveled commitment seller profits'] = leveled_commitment_seller_profits_average
    df.to_csv(file_name,index=False)    

def set_diagram(x_values, y_pure_values, y_leveled_commitment_values, label):
    plt.plot(x_values, y_pure_values, label= label + " (Pure)")
    plt.plot(x_values, y_leveled_commitment_values, label= label + " (Leveled commitment)")

def create_diagram_file(x_label, y_label, title, file_name):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.savefig(file_name)
    plt.close()


def run_experiments():
    #default settings
    k = 25
    n = 30
    r = 5
    s_max = 10.00
    epsilon = 0.25
    bidding_factor_max = 2.0

    #1. experiment: Influence of the number of sellers
    number_sellers = []
    pure_seller_profits_average = []
    leveled_commitment_seller_profits_average = []
    pure_buyer_profits_average = []
    leveled_commitment_buyer_profits_average = []

    for i in range(1, 30):
        number_sellers.append(i)
        simulation = Simulation(i, n, r, s_max, epsilon, AuctionType.PURE, bidding_factor_max)
        simulation.run()
        pure_seller_profits_average.append(simulation.seller_profits_average)
        pure_buyer_profits_average.append(simulation.buyer_profits_average)
        simulation = Simulation(i, n, r, s_max, epsilon, AuctionType.LEVELED_COMMITMENT, bidding_factor_max)
        simulation.run()
        leveled_commitment_seller_profits_average.append(simulation.seller_profits_average)
        leveled_commitment_buyer_profits_average.append(simulation.buyer_profits_average)

    set_diagram(number_sellers, pure_seller_profits_average, leveled_commitment_seller_profits_average, "Sellers")
    set_diagram(number_sellers, pure_buyer_profits_average, leveled_commitment_buyer_profits_average, "Buyers")
    create_diagram_file("Number of sellers", "Average profit", "Increasing number of sellers", "1. experiment.png")
    create_output("Number of sellers" ,"1. experiment.csv", number_sellers, pure_buyer_profits_average, pure_seller_profits_average, leveled_commitment_buyer_profits_average, leveled_commitment_seller_profits_average)


    #2. experiment: Influence of the number of buyers
    number_buyers = []
    pure_seller_profits_average = []
    leveled_commitment_seller_profits_average = []
    pure_buyer_profits_average = []
    leveled_commitment_buyer_profits_average = []

    for i in range(11, 61):
        number_buyers.append(i)
        simulation = Simulation(10, i, r, s_max, epsilon, AuctionType.PURE, bidding_factor_max)
        simulation.run()
        pure_seller_profits_average.append(simulation.seller_profits_average)
        pure_buyer_profits_average.append(simulation.buyer_profits_average)
        simulation = Simulation(10, i, r, s_max, epsilon, AuctionType.LEVELED_COMMITMENT, bidding_factor_max)
        simulation.run()
        leveled_commitment_seller_profits_average.append(simulation.seller_profits_average)
        leveled_commitment_buyer_profits_average.append(simulation.buyer_profits_average)

    set_diagram(number_buyers, pure_seller_profits_average, leveled_commitment_seller_profits_average, "Sellers")
    set_diagram(number_buyers, pure_buyer_profits_average, leveled_commitment_buyer_profits_average, "Buyers")
    create_diagram_file("Number of buyers", "Average profit", "Increasing number of buyers", "2. experiment.png")
    create_output("Number of buyers" ,"2. experiment.csv", number_buyers, pure_buyer_profits_average, pure_seller_profits_average, leveled_commitment_buyer_profits_average, leveled_commitment_seller_profits_average)
    

    #3. experiment: Influence of the number of rounds
    number_rounds = []
    pure_seller_profits_average = []
    leveled_commitment_seller_profits_average = []
    pure_buyer_profits_average = []
    leveled_commitment_buyer_profits_average = []

    for i in range(1, 21):
        number_rounds.append(i)
        simulation = Simulation(k, n, i, s_max, epsilon, AuctionType.PURE, bidding_factor_max)
        simulation.run()
        pure_seller_profits_average.append(simulation.seller_profits_average)
        pure_buyer_profits_average.append(simulation.buyer_profits_average)
        simulation = Simulation(k, n, i, s_max, epsilon, AuctionType.LEVELED_COMMITMENT, bidding_factor_max)
        simulation.run()
        leveled_commitment_seller_profits_average.append(simulation.seller_profits_average)
        leveled_commitment_buyer_profits_average.append(simulation.buyer_profits_average)

    set_diagram(number_rounds, pure_seller_profits_average, leveled_commitment_seller_profits_average, "Sellers")
    set_diagram(number_rounds, pure_buyer_profits_average, leveled_commitment_buyer_profits_average, "Buyers")
    create_diagram_file("Number of rounds", "Average profit", "Increasing number of rounds", "3. experiment.png")
    create_output("Number of rounds" ,"3. experiment.csv", number_rounds, pure_buyer_profits_average, pure_seller_profits_average, leveled_commitment_buyer_profits_average, leveled_commitment_seller_profits_average)
    

    #4. experiment: Influence of the maximum start price
    s_maxs = []
    pure_seller_profits_average = []
    leveled_commitment_seller_profits_average = []
    pure_buyer_profits_average = []
    leveled_commitment_buyer_profits_average = []

    for i in range(10, 610, 10):
        s_maxs.append(i)
        simulation = Simulation(k, n, r, i, epsilon, AuctionType.PURE, bidding_factor_max)
        simulation.run()
        pure_seller_profits_average.append(simulation.seller_profits_average)
        pure_buyer_profits_average.append(simulation.buyer_profits_average)
        simulation = Simulation(k, n, r, i, epsilon, AuctionType.LEVELED_COMMITMENT, bidding_factor_max)
        simulation.run()
        leveled_commitment_seller_profits_average.append(simulation.seller_profits_average)
        leveled_commitment_buyer_profits_average.append(simulation.buyer_profits_average)

    set_diagram(s_maxs, pure_seller_profits_average, leveled_commitment_seller_profits_average, "Sellers")
    set_diagram(s_maxs, pure_buyer_profits_average, leveled_commitment_buyer_profits_average, "Buyers")
    create_diagram_file("Maximum start price", "Average profit", "Increasing maximum start price", "4. experiment.png")
    create_output("Maximum start price" ,"4. experiment.csv", s_maxs, pure_buyer_profits_average, pure_seller_profits_average, leveled_commitment_buyer_profits_average, leveled_commitment_seller_profits_average)
    
    
    #5. experiment: Influence of penalty factor
    epsilons = []
    pure_seller_profits_average = []
    leveled_commitment_seller_profits_average = []
    pure_buyer_profits_average = []
    leveled_commitment_buyer_profits_average = []

    for i in numpy.arange(0, 1.05, 0.05):
        epsilons.append(i)
        simulation = Simulation(k, n, r, s_max, i, AuctionType.PURE, bidding_factor_max)
        simulation.run()
        pure_seller_profits_average.append(simulation.seller_profits_average)
        pure_buyer_profits_average.append(simulation.buyer_profits_average)
        simulation = Simulation(k, n, r, s_max, i, AuctionType.LEVELED_COMMITMENT, bidding_factor_max)
        simulation.run()
        leveled_commitment_seller_profits_average.append(simulation.seller_profits_average)
        leveled_commitment_buyer_profits_average.append(simulation.buyer_profits_average)

    set_diagram(epsilons, pure_seller_profits_average, leveled_commitment_seller_profits_average, "Sellers")
    set_diagram(epsilons, pure_buyer_profits_average, leveled_commitment_buyer_profits_average, "Buyers")
    create_diagram_file("Penalty factor", "Average profit", "Increasing penalty factor", "5. experiment.png")
    create_output("Penalty factor" ,"5. experiment.csv", epsilons, pure_buyer_profits_average, pure_seller_profits_average, leveled_commitment_buyer_profits_average, leveled_commitment_seller_profits_average)
    
       
    #6. experiment: Influence of the maximum bidding factor
    bidding_factor_maxs = []
    pure_seller_profits_average = []
    leveled_commitment_seller_profits_average = []
    pure_buyer_profits_average = []
    leveled_commitment_buyer_profits_average = []

    for i in range(2, 21):
        bidding_factor_maxs.append(i)
        simulation = Simulation(k, n, r, s_max, epsilon, AuctionType.PURE, i)
        simulation.run()
        pure_seller_profits_average.append(simulation.seller_profits_average)
        pure_buyer_profits_average.append(simulation.buyer_profits_average)
        simulation = Simulation(k, n, r, s_max, epsilon, AuctionType.LEVELED_COMMITMENT, i)
        simulation.run()
        leveled_commitment_seller_profits_average.append(simulation.seller_profits_average)
        leveled_commitment_buyer_profits_average.append(simulation.buyer_profits_average)

    set_diagram(bidding_factor_maxs, pure_seller_profits_average, leveled_commitment_seller_profits_average, "Sellers")
    set_diagram(bidding_factor_maxs, pure_buyer_profits_average, leveled_commitment_buyer_profits_average, "Buyers")
    create_diagram_file("Maximum bidding factor", "Average profit", "Increasing maximum bidding factor", "6. experiment.png")
    create_output("Maximum bidding factor" ,"6. experiment.csv", bidding_factor_maxs, pure_buyer_profits_average, pure_seller_profits_average, leveled_commitment_buyer_profits_average, leveled_commitment_seller_profits_average)
    
    
if __name__ == "__main__":
    run_experiments()

    # number of sellers
    k = 30
    # number of buyers
    n = 40
    # number of auction rounds
    r = 10
    # universal maximum starting price
    s_max = 10.00
    # penalty factor
    epsilon = 0.25
    # auction type AuctionType
    type = AuctionType.LEVELED_COMMITMENT
    # maximum bidding factor
    bidding_factor_max = 2.0

    simulation = Simulation(k, n, r, s_max, epsilon, type, bidding_factor_max)
    simulation.run()

    print("Market prices of sellers:")
    for seller in simulation.sellers:
        print(f"Seller: {seller.id}")
        for market_price in seller.market_prices:
            print(market_price)

    print("Profits of sellers:")
    for seller in simulation.sellers:
        print(f"Seller: {seller.id} profit: {seller.profit}")

    print("Profits of buyers:")
    for buyer in simulation.buyers:
        print(f"Buyer: {buyer.id} profit: {buyer.profit}")
