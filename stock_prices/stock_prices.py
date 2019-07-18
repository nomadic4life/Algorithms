#!/usr/bin/python

import argparse


def find_max_profit(prices):

    last = len(prices) - 1
    low = {"index": 0, "value": prices[0]}
    high = {"index": last, "value": prices[last]}

    for i in range(0, len(prices)):

        if prices[i] <= low["value"] and i <= high["index"]:
            low_temp = {"index": i, "value": prices[i]}

        if high["value"] <= prices[last - i] and last - i >= low["index"]:
            high_temp = {"index": last - i, "value": prices[last - i]}

        if high_temp["index"] <= low["index"] and low_temp["index"] >= high["index"]:
            return prices[last] - prices[last - 1]
        else:
            low = low_temp
            high = high_temp

    return (high["value"] - low["value"])


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
