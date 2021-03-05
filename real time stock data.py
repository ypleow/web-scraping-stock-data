# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import datetime
import bs4
import requests
from bs4 import BeautifulSoup


## url = https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    }
def stock_price(stock_code):
    r=requests.get(('https://finance.yahoo.com/quote/') + stock_code + ('?p=') + stock_code + ('.tsrc=fin-srch'), headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    content = soup.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
   
    ##if content == []:
        ##content = '99999'
    
    return content



stock = ['TSLA','FB','AMZN','NFLX']

while True:
    price = []
    time = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for stock_code in stock:
        price.append(stock_price(stock_code))
    time = [time_stamp]
    time.extend(price)
    df = pd.DataFrame(time)
    df = df.T
    ## mode = 'a' >> append mode
    df.to_csv("stock data.csv", mode = 'a', header = False)
    
    print(time)


