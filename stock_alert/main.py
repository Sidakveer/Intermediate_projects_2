import requests
import datetime as dt


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"



params_stocks = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "E1KQTB56ZWFXCSUL"
}


# stock_api = "E1KQTB56ZWFXCSUL"
stock_response = requests.get(url="https://www.alphavantage.co/query", params=params_stocks)
stock_data_daily = stock_response.json()["Time Series (Daily)"]
date_string1 = f"{dt.datetime.today().year}-0{dt.datetime.today().month}-0{dt.datetime.today().day - 2}"
date_string2 = f"{dt.datetime.today().year}-0{dt.datetime.today().month}-0{dt.datetime.today().day - 3}"
stock_price_yesterday = stock_data_daily[date_string1]["4. close"]
stock_price_dayeforeYes = stock_data_daily[date_string2]["4. close"]

diff = float(stock_price_yesterday) - float(stock_price_dayeforeYes)
if diff < 0:
    diff = diff * -1
percent_change = (diff * 100 )/ float(stock_price_yesterday)