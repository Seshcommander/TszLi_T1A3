# Welcome to Peter's Bitcoin Checker!

### Dependencies:

- Python 3
- Pandas + Numpy + python-dateutil + pytz + six

Please check you have the correct version of python using `python --version` in your computer's terminal

### Python 3 Minimum Requirements:

`Processors: Intel® Core™ i3 or AMD Ryzen 3250u CPU Operating System: Windows 7, Linux 64-bit RHEL or Mac OS X 10.11 & up RAM: 1GB of on-board system memory Disk Space: 1-2GB of Hard Drive space` according to (Khan, 2021)

Reference:

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

## Application Walkthrough:

<br>

When the program first runs you will be prompted to a menu:

- Allows you to check price of Bitcoin on the specified input date
- Allows you to compare the bitcoin price at the specific date with the _current date_ (2022-07-15)
- Checks volume of BTC in USDT or BTC at the specified date (BTC/USDT inputs are case sensitive)
- Profit calculator allows you to see how much the user's entered bitcoins were worth at the specified time and shows the profit or loss compared to current prices.

_Fig 1. - Menu_
![menu](./docs/Options%20menu%20interface.png)

Using the keyboard, typing options 1-3 will allow you to enter a date:
<br>

_Figure 1.2. - Option 1 selected and date provided_
![Pricecheck](./docs/price%20check%20interface.png)

_Figure 1.3. - Option 2 selected and date provided_
![Pricecomparison](./docs/Price%20comparison%20interface.png)

_Figure 1.4. - Option 3 selected and date provided_
![volumecheck](./docs/Volume%20Check%20Interface.png)

_Figure 1.5. - Option 4 selected and date provided_
![profitcalc](./docs/Profit%20Calc%20Interface.png)

<br>

## _Errors and testing:_

Common errors in the program include:

1. Not providing date format correctly or entering any date
2. Not providing units correctly (BTC/USDT for volume checker)
3. Not providing values correctly (Profit Calculator)

Error messages will output if the user provides invalid inputs. Please enter inputs carefully

To minimise any errors that may occur, please enter in the format provided.

Below are the testing feature IDS:
![Ids](./docs/Feature%20IDs.png)

Full report can be found in the docs folder:
`docs/Peter Li - T1A3 Testing Report - Test Cases.pdf`

## _Source code repo:_

Full source code repository can be found at:
https://github.com/Seshcommander/TszLi_T1A3

## Implementation Plan:

Source: `docs/T1A3_Peter Li-Implementation_Plan.pdf`

## _References:_

Khan, H., 2022. What Are The Ideal Computer Specs For Python Programming In 2021 – [Brief Guide]. [online] Ssiddique.info. Available at: <https://ssiddique.info/ideal-computer-specs-for-python-programming.html> [Accessed 17 July 2022].
