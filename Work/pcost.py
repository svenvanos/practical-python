# pcost.py
#
# Exercise 1.27
from report import read_portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    total_price = sum([s["shares"] * s["price"] for s in portfolio])
        
    return total_price

def main(args):
    
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    cost = portfolio_cost(args[1])

    print(f"Total price to buy all stocks is ${cost:.2f}")
    
if __name__ == "__main__":
    import sys
    main(sys.argv)