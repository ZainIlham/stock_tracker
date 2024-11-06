import pickle
from Stock import Stock

# stocks = {
#     'ANTM': Stock(lot = 65, avg_price = 1546),
#     'BBCA': Stock(lot = 10, avg_price = 10640.94),
#     'BBRI': Stock(lot = 12, avg_price = 5036.71)
# }

# Load stocks from a file if it exists, otherwise create an empty dictionary
try:
    with open("stocks_data.pkl", "rb") as file:
        stocks = pickle.load(file)
except FileNotFoundError:
    stocks = {}

def save_stocks():
    with open("stocks_data.pkl", "wb") as file:
        pickle.dump(stocks, file)

def get_stocks():
    return stocks