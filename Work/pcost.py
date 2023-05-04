# pcost.py
#
# Exercise 1.27
import sys
from report import read_portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    total_price = sum([s["shares"] * s["price"] for s in portfolio])
        
    return total_price


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)

print(f"Total price to buy all stocks is ${cost:.2f}")