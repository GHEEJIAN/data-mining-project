# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:34:59 2019

@author: LENOVO
"""

#make sure selenium is installed via cmd
#make sure chromedriver is installed in the machine

#write down the location of chromedriver
wd = '______________/chromedriver'

# import package
from selenium import webdriver

browser = webdriver.Chrome(wd) # open web page
browser.implicitly_wait(10) # wait for web page to load

company_names = [] # save company names in a list
# crawl all company names from A-Z
for i in range(65,91):
    url = 'https://www.thestar.com.my/business/marketwatch/stock-list/?alphabet='+chr(i)
    browser.get(url)
    
    name_list = browser.find_elements_by_xpath('//table[@class="market-trans"]//tr[@class="linedlist"]/td/a')
    for name in name_list:
        if name.text!='':
            name_text = name.text.replace("&","%26") 
            company_names.append(name_text)

# crawl all company names in 0-9
url1 = 'https://www.thestar.com.my/business/marketwatch/stock-list/?alphabet=0-9'
browser.get(url1)
name1_list = browser.find_elements_by_xpath('//table[@class="market-trans"]//tr[@class="linedlist"]/td/a')
for name1 in name1_list:
    if name1.text!='':
        name1_text = name1.text.replace("&","%26") 
        company_names.append(name1_text)

#print(company_names)
browser.close()

# save as links for crawling all the information
company_links = []
for n in company_names:
    link = 'https://www.thestar.com.my/business/marketwatch/stocks/?qcounter=' + n
    company_links.append(link)