# report.py
#
# Exercise 2.4

import fileparse

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    return fileparse.parse_csv(filename, select=["name", "shares", "price"], types=[str, int, float])


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))


def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report_list = []
    for s in portfolio:
        pre = s["price"]
        current = prices[s["name"]]
        change = current - pre
        report_list.append((s["name"], s["shares"], prices[s["name"]], change))
    return report_list


def print_report (report):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    print("%10s %10s %10s %10s" % ("Name", "Shares", "Price", "change"))
    print("%10s %10s %10s %10s" % ("----------", "----------", "----------", "----------"))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$"+str(round(price, 2)):>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

