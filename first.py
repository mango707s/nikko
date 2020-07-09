import alpha_vantage
from alpha_vantage import *
import json
import requests
import csv

API_URL = "https://www.alphavantage.co/query" 
symbols = ['QCOM',"INTC","PDD","AAPL"]

for symbol in symbols:
        data = { "function": "TIME_SERIES_INTRADAY", 
        "symbol": symbol,
        "interval" : "60min",       
        "datatype": "json", 
        "apikey": "xx" } 
        response = requests.get(API_URL, data) 
        data = response.json()
        print(symbol)
        a = (data['Time Series (60min)'])
        keys = (a.keys())
        for key in keys:
                print(a[key]['2. high'] + " " + a[key]['5. volume'])

SomeCommand > SomeFile.txt  

