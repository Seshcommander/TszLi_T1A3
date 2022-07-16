# Welcome to Peter's Bitcoin Checker!

### Dependencies:

- Python 3
- Pandas + Numpy + python-dateutil + pytz + six

Please check you have the correct version of python using `python --version` in your computer's terminal

### Application Installation steps:

<br>

#### <u>Virtual env (preferred)</u>

1. Ensure Python 3 is installed (refer to https://www.python.org/downloads/)
2. Run command `./run-project.sh` in your OS terminal or double click run-project.sh

_\*Note that virtual environment is preferred for users who do not want to install or overwrite the dependencies on their native system_

#### <u>Native</u>

1. Run the command `pip install -r requirements.txt` in your terminal
2. Run command `python src/main.py`

_\*Warning! Installing the dependencies on your native system may override the current versions which may cause other programs to not function correctly, please check your versions before proceeding._

<br>

### Application Walkthrough:

<br>

When the program first runs you will be prompted to a menu:

- Allows you to check price of Bitcoin on the specified date
- Allows you to compare a specific date with the _current date_ (2022-07-07)
- Checks volume of BTC in USDT or BTC at the specified date
- Profit calculator allows you to see whether you have made a profit or not based on the number of bitcoins you had

_Fig 1. Menu_
![menu](

Using the keyboard, typing options 1-3 will allow you to enter a date:
<br>

_Figure 1.2. Option 1 selected and date provided_
![Pricecheck](./docs/price%20check%20interface.png)

_Figure 1.3. Option 2 selected and date provided_
![Pricecomparison](./docs/Price%20comparison%20interface.png)

_Figure 1.4. Option 3 selected and date provided_
