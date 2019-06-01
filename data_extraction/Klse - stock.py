# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:32:11 2019

@author: user
"""
#make sure selenium is installed via cmd
#make sure chromedriver is installed in the machine

#write down the location of chromedriver
wd = '________________/chromedriver'

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

page = requests.get('https://www.klsescreener.com/v2/financial-reports')
soup = BeautifulSoup(page.text, 'html.parser')
stock_table = soup.find(class_='table table-striped') #specify the location
urls = []
for a in stock_table.find_all('a'):   #find all 'a' from the specified location
    urls.append(a.attrs['href'])      #extract attribute inside 'a'

even_list = [] 
for i in range (0,len(urls)-1):       #only links at even number index is required
    if i % 2 == 0:
        even_list.append(urls[i])

link_front = 'https://www.klsescreener.com'      
even_link = [link_front + s for s in even_list]       #add https:// to the links

fullname_list = []
name_list = []
category_list = []
w52_list = []
ROE_list = []
PE_list = []
EPS_list = []
DPS_list = []
DY_list = []
PTBV_list = []
RPS_list = []
PSR_list = []
Market_Cap_list = []
RSI_list = []
Stochastic_list = []


driver = webdriver.Chrome(wd)

for l in even_link:
        driver.get(l)
        driver.implicitly_wait(10)
        fullname = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/span')
        name = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]')
        category = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/span[2]')
        w52 = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[7]/td[2]')
        ROE = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[8]/td[2]')
        PE = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[9]/td[2]')
        EPS = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[10]/td[2]')
        DPS = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[11]/td[2]')
        DY = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[12]/td[2]')
        PTBV = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[14]/td[2]')
        RPS = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[15]/td[2]')
        PSR = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[16]/td[2]')
        Market_Cap = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[1]/tbody/tr[17]/td[2]')
        RSI = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[3]/tbody/tr[1]/td[2]')
        Stochastic = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/table[3]/tbody/tr[2]/td[2]')
        
        fullname1 = fullname.text
        fullname_list.append(fullname1)
        
        name1 = name.text
        name_list.append(name1)
        
        category1 = category.text
        category_list.append(category1)
        
        
        w521 = w52.text
        w52_list.append(w521)
        
        ROE1 = ROE.text
        ROE_list.append(ROE1)
        
        PE1 = PE.text
        PE_list.append(PE1)
        
        EPS1 = EPS.text
        EPS_list.append(EPS1)
        
        DPS1 = DPS.text
        DPS_list.append(DPS1)
        
        DY1 = DY.text
        DY_list.append(DY1)
        
        PTBV1 = PTBV.text
        PTBV_list.append(PTBV1)
        
        RPS1 = RPS.text
        RPS_list.append(RPS1)
        
        PSR1 = PSR.text
        PSR_list.append(PSR1)
        
        Market_Cap1 = Market_Cap.text
        Market_Cap_list.append(Market_Cap1)
        
        RSI1 = RSI.text
        RSI_list.append(RSI1)
        
        Stochastic1 = Stochastic.text
        Stochastic_list.append(Stochastic1)
        
        

import pandas as pd

dataframe = pd.DataFrame({'full name':fullname_list,'name':name_list,'category':category_list,'52w':w52_list, 
                          'ROE':ROE_list, 'P/E':PE_list,'EPS':EPS_list, 'DPS':DPS_list, 'DY':DY_list, 
                          'PTBV':PTBV_list, 'RPS':RPS_list, 'PSR':PSR_list, 'Market_Cap':Market_Cap_list, 
                          'RSI':RSI_list, 'Stochastic':Stochastic_list})

dataframe.to_csv('stock_klse.csv', index = False, sep = ',')        