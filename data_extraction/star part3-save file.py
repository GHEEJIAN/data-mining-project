# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:36:55 2019

@author: LENOVO
"""

import pandas as pd

na = name_list
co = code_list
da = date_list
ti = time_list
op = open_price_list
lo = low_list
hi = high_list
pr = price_list
vo = vol_list
bv = buy_vol_list
sv = sell_vol_list

dataframe = pd.DataFrame({'name':na,'code':co,'date':da,'time':ti,'open':op,'low':lo,'high':hi,'price':pr,'volume':vo,'buy/volum':bv,'sell/volum':sv})

# save data
dataframe.to_csv("Stock Crawling-Day 2.csv",index=False,sep=',')
