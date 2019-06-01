# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:35:54 2019

@author: LENOVO
"""

# import packages
from lxml import html
import requests

class AppCrawler:
    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.apps = []

    def crawl(self):
        self.get_app_from_link(self.starting_url)
        return

    def get_app_from_link(self, link):
        start_page = requests.get('https://www.thestar.com.my/business/marketwatch/stocks/?qcounter=A50CHIN-C26')
        tree = html.fromstring(start_page.text)
        name = tree.xpath('//h1[@class="stock-profile f16"]/text()')[0]
        price = tree.xpath('//td[@id="slcontent_0_ileft_0_lastdonetext"]/text()')[0]
        code = tree.xpath('//li[@class="f14"]/text()')[1]
        date = tree.xpath('//span[@id="slcontent_0_ileft_0_datetxt"]/text()')[0]
        time = tree.xpath('//span[@id="slcontent_0_ileft_0_timetxt"]/text()')[0]
        open_price = tree.xpath('//td[@id="slcontent_0_ileft_0_opentext"]/text()')[0]
        low = tree.xpath('//td[@id="slcontent_0_ileft_0_lowtext"]/text()')[0]
        high = tree.xpath('//td[@id="slcontent_0_ileft_0_hightext"]/text()')[0]
        vol = tree.xpath('//td[@id="slcontent_0_ileft_0_voltext"]/text()')[0]
        buy_vol = tree.xpath('//td[@id="slcontent_0_ileft_0_buyvol"]/text()')[0]
        sell_vol = tree.xpath('//td[@id="slcontent_0_ileft_0_sellvol"]/text()')[0]

        name_list.append(name)
        #print(name)
        code_list.append(code[3:])
        #print(code[3:])
        price_list.append(price)
        #print(price)
        date_list.append(date[10:21])
        #print(date[10:21])
        time_list.append(time)
        #print(time)
        open_price_list.append(open_price)
        #print(open_price)
        low_list.append(low)
        #print(low)
        high_list.append(high)
        #print(high)
        vol_list.append(vol)
        #print(vol)
        buy_vol_list.append(buy_vol)
        #print(buy_vol)
        sell_vol_list.append(sell_vol)
        #print(sell_vol)
        
        return
    
class App:

    def __init__(self, name, code, price, links):
        self.name = name
        self.code = code
        self.price = price
        self.links = links

    def __str__(self):
        return ("Name: " + self.name.encode('UTF-8') +
        "\r\nCode: " + self.developer.encode('UTF-8') +
        "\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")
    
# create list for all the variables
name_list = []
code_list = []
price_list = []
date_list = []
time_list = []
open_price_list = []
low_list = []
high_list = []
vol_list = []
buy_vol_list = []
sell_vol_list = []

for l in company_links:
    crawler = AppCrawler(l, 0)
    crawler.crawl()