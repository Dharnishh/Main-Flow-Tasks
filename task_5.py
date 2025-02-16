import random

class StockMarketSimulator:
    def __init__(self):
        self.stocks = {'AAPL': 100, 'GOOG': 1500, 'TSLA': 700}
        self.users = {}
    
    def register_user(self, username, initial_balance):
        self.users[username] = {'balance': initial_balance, 'portfolio': {}}
    
    def buy_stock(self, username, stock, quantity):
        user = self.users.get(username)
        if user:
            stock_price = self.stocks.get(stock)
            cost = stock_price * quantity
            if user['balance'] >= cost:
                user['balance'] -= cost
                user['portfolio'][stock] = user['portfolio'].get(stock, 0) + quantity
                print(f"{username} bought {quantity} shares of {stock}.")
            else:
                print(f"Insufficient balance.")
    
    def sell_stock(self, username, stock, quantity):
        user = self.users.get(username)
        if user:
            stock_price = self.stocks.get(stock)
            if user['portfolio'].get(stock, 0) >= quantity:
                user['portfolio'][stock] -= quantity
                user['balance'] += stock_price * quantity
                print(f"{username} sold {quantity} shares of {stock}.")
            else:
                print(f"Not enough shares to sell.")
    
    def update_stock_prices(self):
        for stock in self.stocks:
            self.stocks[stock] = round(self.stocks[stock] * (1 + random.uniform(-0.05, 0.05)), 2)
    
    def get_user_portfolio(self, username):
        return self.users.get(username)
    
    def __str__(self):
        return str(self.stocks)

# Example usage
simulator = StockMarketSimulator()
simulator.register_user('Alice', 10000)
simulator.buy_stock('Alice', 'AAPL', 10)
simulator.update_stock_prices()
simulator.sell_stock('Alice', 'AAPL', 5)
print(simulator.get_user_portfolio('Alice'))
print(simulator)
