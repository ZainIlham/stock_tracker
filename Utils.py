from MyStocks import *

stocks = get_stocks()

def print_my_stocks():
    if not stocks:
        print("\nNo stocks in portfolio.")
        return

    print("\nMy Stocks:")
    print(f"{'Symbol':<10} {'Lot':<10} {'Avg Price':<10} {'Invested':<10}")
    print("-" * 50)

    for symbol, stock in stocks.items():
        invested_value = stock.avg_price * stock.lot * 100
        print(f"{symbol:<10} {stock.lot:<10} {stock.avg_price:<10.2f} {format_currency(invested_value)}")

    input("\nPress Enter to return to the main menu...")

def buy_stock():
    symbol = input("Enter stock symbol (or '0' to go back): ").upper()
    if symbol == "0":
        return

    try:
        lot = int(input("Enter number of lots to buy (or '0' to go back): "))
        if lot == 0:
            return
        price = float(input("Enter purchase price per lot (or '0' to go back): "))
        if price == 0:
            return

        if symbol in stocks:
            stock = stocks[symbol]
            total_lots = stock.lot + lot
            total_investment = (stock.lot * stock.avg_price) + (lot * price)
            stock.avg_price = total_investment / total_lots
            stock.lot = total_lots
        else:
            stocks[symbol] = Stock(lot=lot, avg_price=price)
        
        save_stocks()
        print(f"{symbol} added/updated successfully.")

    except ValueError:
        print("Invalid input. Please enter a number.")

    input("\nPress Enter to return to the main menu...")

def sell_stock():
    symbol = input("Enter stock symbol to sell (or '0' to go back): ").upper()
    if symbol == "0":
        return
    if symbol not in stocks:
        print("Stock not found in portfolio.")
        return

    try:
        stock = stocks[symbol]

        lot = int(input(f"You have {stock.lot} lots. Enter number of lots to sell (or '0' to go back): "))
        if lot == 0:
            return
        
        if lot > stock.lot:
            print(f"Cannot sell more than owned. You have {stock.lot} lots.")
            return

        stock.lot -= lot
        if stock.lot == 0:
            del stocks[symbol]  # Remove stock if no lots left
        save_stocks()
        print(f"{lot} lot of {symbol} sold successfully.")
        
    except ValueError:
        print("Invalid input. Please enter a number.")

    input("\nPress Enter to return to the main menu...")

def calculate_new_avg_price():
    symbol = input("Enter stock symbol you intend to buy (or '0' to go back): ").upper()
    if symbol == "0":
        return
    if symbol not in stocks:
        print("Stock not found in portfolio.")
        return

    try:
        stock = stocks[symbol]

        new_lot = int(input(f"You have {stock.lot} lots. Enter number of lots you intend to buy (or '0' to go back): "))
        if new_lot == 0:
            return
        new_price = float(input("Enter purchase price per lot you intend to buy (or '0' to go back): "))
        if new_price == 0:
            return

        total_investment_before = stock.avg_price * stock.lot
        total_investment_new_purchase = new_price * new_lot
        total_investment_after = total_investment_before + total_investment_new_purchase
        total_lots_after = stock.lot + new_lot
        new_avg_price = total_investment_after / total_lots_after

        print(f"The avg price of {symbol} will be changed from {stock.avg_price} to {new_avg_price}")

    except ValueError:
        print("Invalid input. Please enter a number.")

    input("\nPress Enter to return to the main menu...")

def calculate_net_gain_value():
    symbol = input("Enter stock symbol you want to sell (or '0' to go back): ").upper()
    if symbol == "0":
        return
    if symbol not in stocks:
        print("Stock not found in portfolio.")
        return

    try:
        while True:
            stock = stocks[symbol]

            lots = int(input(f"You have {stock.lot} lots. Enter number of lots you want to sell (or '0' to go back): "))
            if lots == 0:
                return


            if lots > stock.lot:
                print(f"The maximum lots you have for {symbol} is {stock.lot} lots.\n")
            else:
                break  # Exit loop if the entered lots are valid

        sell_price = float(input("Enter sell price (or '0' to go back): "))
        if sell_price == 0:
            return

        shares = lots * 100
        total_purchase = stock.avg_price * shares
        total_selling = sell_price * shares
        tax = total_selling * 0.0025
        net_total_selling = total_selling - tax
        net_gain = net_total_selling - total_purchase
        perc_gain = round((net_gain / total_purchase) * 100, 2)

        print(f"If you sell {lots} lots of {symbol} at price {sell_price}, you will gain :\n - Total value {format_currency(net_total_selling)} \n - With profit {format_currency(net_gain)} \n - Increased by {perc_gain}% ")
    except ValueError:
        print("Invalid input. Please enter a number.")

    input("\nPress Enter to return to the main menu...")

def calculate_dividend():
    symbol = input("Enter stock symbol (or '0' to go back): ").upper()
    if symbol == "0":
        return
    if symbol not in stocks:
        print("Stock not found in portfolio.")
        return

    try:
        price = int(input("Enter dividend price per share in rupiah (or '0' to go back): "))
        if price == 0:
            return

        stock = stocks[symbol]

        shares = stock.lot * 100
        total_dividend = price * shares

        print(f"You have {shares} shares of {symbol} and will receive dividend {format_currency(total_dividend)}")
    except ValueError:
        print("Invalid input. Please enter a number.")

    input("\nPress Enter to return to the main menu...")

def format_currency(value):
    """Format the currency to Indonesian Rupiah format."""
    return f"Rp. {value:,.0f}".replace(",", ".")