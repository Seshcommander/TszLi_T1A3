# imported pandas library as pd and system from operating system
from os import system
import pandas as pd

# dataframe variable (df) assigned to pd.read_csv function with input parameters specifying file location, columns, formatting of dates and data type of columns
df = pd.read_csv(
    "docs/BTCUSDT.csv",
    parse_dates=["date"],
    date_parser=lambda x: pd.to_datetime(x, format="%Y-%m-%d %H:%M:%S"),
    usecols=[
        "unix", "date", "symbol", "open", "high", "low", "close", "Volume BTC", "Volume USDT"], dtype={
        "unix": int, "date": str, "symbol": str, "open": float, "high": float, "low": float, "close": float, "Volume BTC": float, "Volume USDT": float
    })

# Welcome message to user


def welcome_message():
    print("Welcome to Peter's BTC historical data checker \n To begin, please select from the following options:")


# function to display options 1-4 for the user to select
def print_options():
    print("1) Check historical price")
    print("2) Price comparison between today and entered date")
    print("3) Check volume")
    print("4) Profit Calculator")
    print("5) Exit")
    option = input("Select your option (1-5): ")
    return option


#  Function that takes a date of the user's choosing and returns the user_date variable
def user_input_date():
    user_date = input("Please enter a date in the format (YYYY-MM-DD): ")
    if len(user_date) < 11 and len(user_date) > 0:
        try:
            user_date_dt = pd.to_datetime(
                user_date, format="%Y-%m-%d %H:%M:%S")
            return user_date_dt
        except Exception as e:
            print("That is not a valid date format")
            return False
    else:
        print("Incorrect date length. Please provide date in correct format (YYYY-MM-DD)")
    return False


# price check input function calls on the user_input_date function and saves it as user_date

def price_check_input():
    user_date = user_input_date()
    if user_date:
        date_price = float(df.loc[(df['date'] == user_date)]['close'])
        print(f"The price of BTC on the {user_date} was ${int(date_price)}")
    # df.loc locates the column with the date exactly matching the user's input date and prints out the closing price column as a float

# price comparison function stores user's input date called by the function into a variable.
# Additional operations performed on the closing price of the user's entered date and compares it with the current date


def price_comparison():
    user_comparison_date = user_input_date()
    if user_comparison_date:
        user_close_price = float(
            df.loc[(df['date'] == user_comparison_date)]['close'])

        current_close_price = float(
            df.loc[(df['date'] == '2022-07-15')]['close'])

        difference = user_close_price - current_close_price

        percentdiff = (difference / current_close_price) * 100
        if percentdiff < 0:
            print(
                f"The price of BTC currently: ${int(current_close_price)} has decreased by {int(percentdiff)}% since {user_comparison_date}")
        elif percentdiff > 0:
            print(
                f"On the {user_comparison_date}, the price of BTC was ${user_close_price} and has increased by {int(percentdiff)}% compared to the current price: ${int(current_close_price)} ")
        elif percentdiff == 0:
            print(
                f"The price of BTC at {user_comparison_date} is the same as the current price.")

    # this functions purpose is to allow the user to enter a date they want the price of btc at and it will calculate the % gain/loss against the most recent updated price (line 2 of the CSV)

# simple function to check volume of BTC at a given date.


def volume_check_input():
    volume_input_date = user_input_date()
    if volume_input_date:
        print("Please select which volumes to check!")
        volume_input = input("BTC or USDT?: ")
        if volume_input == "BTC":
            user_date_vol = float(
                df.loc[(df['date'] == volume_input_date)]['Volume BTC'])
            print(
                f"The volume of Bitcoin traded on {volume_input_date} was {int(user_date_vol)} BTC")
        elif volume_input == "USDT":
            user_date_vol = float(
                df.loc[(df['date'] == volume_input_date)]['Volume USDT'])
            print(
                f"The trading volume of Bitcoin in USDT on {volume_input_date} is {int(user_date_vol)} USDT")
        else:
            print("That is not a valid unit")

# Profit calculator takes user input date and also how much BTC they enter and calculate the value of it at the specified date and compare it to current date.
# Also shows profit/loss depending on if number is > 0 or < 0


def is_number(input):
    try:
        value = float(input)
        if value >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def profit_calculator():
    profit_input_date = user_input_date()
    if profit_input_date:
        print("Please enter how much BTC you had at that date")
        user_btc = input("Amount of BTC: ")
        if is_number(user_btc):
            ref_price = float(
                df.loc[(df['date'] == profit_input_date)]['close'])
            user_profit = float((user_btc)) * float(ref_price)
            current_price = float(
                df.loc[(df['date'] == '2022-07-15')]['close'])
            current_profit = float((user_btc)) * float(current_price)
            profit_diff = current_profit - user_profit
            print(
                f"If you had {user_btc} bitcoins on {profit_input_date}, it would've been worth ${int(user_profit)} and is currently worth ${int(current_profit)}")
            if profit_diff > 0:
                print(
                    f"Your profits since {profit_input_date} are: ${int(profit_diff)}")
            elif profit_diff < 0:
                print(
                    f"Your losses since {profit_input_date} are: ${int(profit_diff)}")
            elif profit_diff == 0:
                print(
                    f"You have made no profits or losses since ${profit_input_date}")
        else:
            print(
                "That is not a valid entry, please enter a numeric value greater than zero")


        # Below is a while loop that checks if the user selects the option and then calls the corresponding function
option = ""

while option != "5":
    system("clear")
    welcome_message()
    option = print_options()
    system("clear")
    if option == "1":
        price_check_input()
    elif option == "2":
        price_comparison()
    elif option == "3":
        volume_check_input()
    elif option == "4":
        profit_calculator()
    elif option == "5":
        continue
    else:
        print("Invalid option")

    input("Press Enter to continue...")
    system("clear")

print("Goodbye have a great time!")
