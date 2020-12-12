import numpy as np
import matplotlib.pyplot as plt
import os


color_list = ["red", "green", "blue", "black", "orange"]


def plot_graph_result(test_name, label, round_list, value_list, step, show=False):
    plt.suptitle(test_name)
    plt.xlabel("rounds")

    if label == "market_price":
        plt.ylabel("price")
    else:
        plt.ylabel("profit")

    if step:
        round_list = [val for i, val in enumerate(round_list) if not i % step ]
        value_list = [val for i, val in enumerate(value_list) if not i % step ]

    plt.plot(round_list, value_list, label=label.replace("_", " "), color="green")


    plt.legend(loc='upper left')

    plt.savefig(f"imgs/graph_test_{test_name}_{label}")

    if show:
        plt.show()

    plt.close()


def plot_value_comparison(test_name, round_list, market_list, seller_list, buyer_list, step, show=False):
    plt.suptitle("SELLER/BUYER comparison: " + test_name)
    plt.xlabel("rounds")
    plt.ylabel("profit")
    if step:
        round_list = [val for i, val in enumerate(round_list) if not i % step ]
        #market_list = [val for i, val in enumerate(market_list) if not i % step ]
        seller_list = [val for i, val in enumerate(seller_list) if not i % step]
        buyer_list = [val for i, val in enumerate(buyer_list) if not i % step ]


    #plt.plot(round_list, market_list, label="market_avg", color="green")
    plt.plot(round_list, seller_list, label="seller_avg", color="red")
    plt.plot(round_list, buyer_list, label="buyer_avg", color="blue")


    plt.legend(loc='upper left')

    plt.savefig(f"imgs/graph_comparison_{test_name}")

    if show:
        plt.show()

    plt.close()


def plot_diff_results(test_name, round_list, label_list, market_set, seller_set, buyer_set, step, show, fig_title = ""):

    lines = []
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))

    if fig_title:
        fig.suptitle(fig_title)

    if step:
        round_list = [val for i, val in enumerate(round_list) if not i % step]

    ax1.set_title('Market Price comparison')
    ax1.set_ylabel('price')
    ax1.set_xlabel('rounds')
    for i, market in enumerate(market_set):
        if step:
            market = [val for i, val in enumerate(market) if not i % step]
        ln = ax1.plot(round_list, market, label=label_list[i], color=color_list[i % len(color_list)])[0]
        lines.append(ln)

    ax2.set_title('Seller Profit comparison')
    ax2.set_ylabel('profit')
    ax2.set_xlabel('rounds')
    for i, seller in enumerate(seller_set):
        if step:
            seller = [val for i, val in enumerate(seller) if not i % step]
        ax2.plot(round_list, seller, label=label_list[i], color=color_list[i % len(color_list)])[0]

    ax3.set_title('Buyer Profit comparison')
    ax3.set_ylabel('profit')
    ax3.set_xlabel('rounds')
    for i, buyer in enumerate(buyer_set):
        if step:
            buyer = [val for i, val in enumerate(buyer) if not i % step]
        ax3.plot(round_list, buyer, label=label_list[i], color=color_list[i % len(color_list)])[0]

    fig.legend(lines,
               label_list,
               loc="center left",
               borderaxespad=0.5,
               title="Legend"
               )

    plt.savefig(f"imgs/graph_test_{test_name}")

    if show:
        wm = plt.get_current_fig_manager()
        if os.name == 'nt':
            wm.window.state('zoomed')
        plt.show()

    plt.close()