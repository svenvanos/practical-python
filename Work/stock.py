# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"

    def cost(self):
        return self.shares * self.price
        
    def sell(self, nshares):
        self.shares -= nshares
        
class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Check the call to "super" and "__init__"
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)
        
    def cost(self):
        # Check the call to "super"
        actual_cost = super().cost()
        return self.factor * actual_cost