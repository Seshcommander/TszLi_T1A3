from os import system
import pandas as pd
import numpy as np

# imported pandas library as pd
data = pd.read_csv(
    "/Users/petey/CoderAcademy/TszLi_T1A3/docs/btcusdt.csv", usecols=[
        "unix", "date", "symbol", "open", "high", "low", "close", "Volume BTC", "Volume USDT"], dtype={
            "unix": int, "date": str, "symbol": str, "open": float, "high": float, "low": float, "close": float, "Volume BTC": float, "Volume USDT": float
    })
# dataframe variable assigned to pd.read_csv function with input parameters specifying file location, columns and data types


def welcome_message_BTC():
    print("Welcome to the BTC historical price/volume checker!\n To begin, please select from the following options:")
# Welcome message to user

# function to display options 1-4, user input is saved as opt var


def print_options():
    print("1) Check historical price of BTC")
    print("2) Price comparison between two dates")
    print("3) Check volume of BTC")
    print("4) Exit")
    opt = input("Select your option (1-4): ")
    return opt

# price check input function to receive user input and save it to a var. Then returns the var so we can access outside of function


def user_input_date():
    user_date = input("Please enter a date in the format (YYYY-MM-DD): ")
    return user_date


user_entered_date = user_input_date


def price_check_input():
    pass
# At a loss for how price check input can take user_enetered_date var and check it against the pd data frame of the csv.
# As per above, need to have a way of matching user_date YYYY-MM-DD to the corresponding row that has the exact date


def price_comparison():
    pass
# this functions purpose is to allow the user to enter a date they want the price of btc at and it will calculate the % gain/loss against the most recent updated price (line 2 of the CSV)


def volume_check_input():
    pass
# simple function to check volume of BTC at a given date.


# Below is just how i would create a menu in terminal for the user to select an option and then be directed to the function that takes the input.
option = ""

while option != "4":
    system("clear")
    welcome_message_BTC()
    option = print_options()
    system("clear")
    if option == "1":
        user_input_date()
        print(user_entered_date)
    elif option == "2":
        price_comparison()
    elif option == "3":
        volume_check_input()
    elif option == "4":
        continue
    else:
        print("Invalid option")

    input("Press Enter to continue...")
    system("clear")

# using the below to print the csv in pandas df for testing. will not print before the options menus (line 74 and above)
df = pd.DataFrame(data)
print(df)

print("Goodbye have a great time!")
