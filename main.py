from Utils import *

def main_menu():
    while True:
        print("\nMenu")
        print("[1] Print My Stocks")
        print("[2] Buy Stock")
        print("[3] Sell Stock")
        print("[4] Calculate New Avg Price")
        print("[5] Calculate Net Gain Value")
        print("[6] Calculate Dividend")
        print("[0] Exit")

        choise = input("Enter your choise: ")

        if choise == "1":
            print_my_stocks()
        elif choise == "2":
            buy_stock()
        elif choise == "3":
            sell_stock()
        elif choise == "4":
            calculate_new_avg_price()
        elif choise == "5":
            calculate_net_gain_value()
        elif choise == "6":
            calculate_dividend()
        elif choise == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choise. Please try again")

if __name__ == "__main__":
    main_menu()