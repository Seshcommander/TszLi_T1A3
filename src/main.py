from os import system
import pandas as pd

# imported pandas library as pd
df = pd.read_csv(
    "/Users/petey/CoderAcademy/TszLi_T1A3/docs/btcusdt.csv", usecols=[
        "unix", "date", "symbol", "open", "high", "low", "close", "Volume BTC", "Volume USDT"], dtype={
            "unix": int, "date": str, "symbol": str, "open": float, "high": float, "low": float, "close": float, "Volume BTC": float, "Volume USDT": float
    })
# dataframe variable assigned to pd.read_csv function with input parameters specifying file location, columns and data types


def welcome_message_BTC():
    print("Welcome to the BTC historical price/volume checker!\n To begin, please select from the following options:")
# Welcome message to user


# welcome_message_BTC()

# function to display options 1-4, user input is saved as opt var


def print_options():
    print("1) Check historical price of BTC")
    print("2) Price comparison between two dates")
    print("3) Check volume of BTC")
    print("4) Exit")
    opt = input("Select your option (1-4): ")
    return opt

# price check input function to receive user input and check against


def user_input_date():
    user_date = input("Please enter a date in the format (YYYY-MM-DD): ")
    return user_date


date_to_check = user_input_date


def price_check_input():
    # df.loc[df["date"] == date_to_check]
    # return
    pass


def price_comparison():
    pass


def volume_check_input():
    pass


option = ""

while option != "4":
    system("clear")
    option = print_options()
    system("clear")
    if option == "1":
        user_input_date()
        price_check_input()
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
# print(df[["date", "close"]])
print()
print("Goodbye have a great time!")
