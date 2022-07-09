import pandas as pd
# imported pandas library as pd
df = pd.read_csv(
    "/Users/petey/CoderAcademy/TszLi_T1A3/docs/btcusdt.csv", usecols=[
        "unix", "date", "symbol", "open", "high", "low", "close", "Volume BTC", "Volume USDT"], dtype={
            "unix": int, "date": str, "symbol": str, "open": float, "high": float, "low": float, "close": float, "Volume BTC": float, "Volume USDT": float
    })
# dataframe variable assigned to pd.read_csv function with input parameters specifying file location, columns and data types
# print(df["date"].dtypes)


def welcome_message_BTC():
    print("Welcome to the BTC historical price/volume checker!\n To begin, please select from the following options:")


welcome_message_BTC()


def print_options():
    print("1) Check historical price of BTC")
    print("2) Price comparison between two dates")
    print("3) Check volume of BTC")
    print("4) Exit")


opt = input("Select your option (1-4): ")


def price_check_input():
    print(f"")


def price_comparison():
    pass


def volume_check_input():
    pass
