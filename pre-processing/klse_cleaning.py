# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:42:13 2019

@author: user
"""
##please write the path of this folder
path = "_____________________/pre-processing/"
import pandas as pd
import os
import re
import numpy as np

#list all files for financial statistics
data = os.listdir(path + 'financial_statistics')

#append all files together
appended_data = []
for i in data:
    df = pd.read_csv(path + 'financial_statistics/'+i)
    appended_data.append(df)
appended_data = pd.concat(appended_data, axis = 0)

#select unique data from dataset
appended_data = appended_data.drop_duplicates()

#to extract code from 'name' variable
codeList = []
for each in appended_data['name']:
    code1 = re.findall(r"\(([0-9]+)\)", each)
    codeList.append(code1)

code = pd.DataFrame({'code': codeList})
code.code = code.code.apply(lambda y: np.nan if len(y)==0 else y)

codeList1 = []
for j in codeList:
    if j == []:
        j = ['nan']
    else:
        j = j
    codeList1.append(j)
flat_list = [item for sublist in codeList1 for item in sublist]

#add variable 'code' to dataframe
appended_data['code'] = flat_list
#remove variable 'name' from dataframe
appended_data = appended_data.drop('name', axis = 1)

#separate category into variable sector_main and sector
new = appended_data['category'].str.split('-', n = 1, expand = True)
appended_data['Sector_main'] = new[1]
appended_data['sector'] = new[0]
#remove variable 'category' from dataframe
appended_data = appended_data.drop('category', axis = 1)

#rearrange columns
#print(appended_data.columns.values)
cols =['full name', 'code', 'Sector_main', 'sector', '52w', 'ROE', 'P/E', 'EPS', 'DPS', 'DY', 'PTBV', 'RPS', 'PSR', 'Market_Cap', 'RSI', 'Stochastic']
appended_data = appended_data[cols]

#write to csv
appended_data.to_csv('klse_clean.csv', index = False)













