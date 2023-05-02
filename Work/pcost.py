# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    with open(filename, "rt") as f:
        headers = next(f)
        rows = csv.reader(f)
        
        total_price = 0
    
        for row in rows:
            try:
                total_price += int(row[1]) * float(row[2])
            except ValueError:
                print("missing field in file")
                
    return total_price


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)

print(f"Total price to buy all stocks is ${cost:.2f}")