#make sure selenium is installed via cmd
#make sure chromedriver is installed in the machine

#write down the location of chromedriver
wd = '________________/chromedriver'

# import package
from selenium import webdriver
from lxml import html
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

name_list = []
code_list = []
sector_1_list = []
sector_2_list = []

sector_list = []
sector_name_list = []
sector_elements = []
sector_links = []
company_names = []
company_links = []


def get_sectors():
    # set up browser
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(wd,options=chrome_options)
    # browser = webdriver.Chrome() # open web page
    browser.implicitly_wait(10)  # wait for web page to load

    url = 'https://www.thestar.com.my/business/marketwatch/'
    browser.get(url)
    r = browser.page_source
    html = BeautifulSoup(r, 'html.parser')
    # print(html)
    browser.close()

    # sector elements
    htmlPart = html.find(class_=re.compile("stocks"))
    linkPart = [x.get_attribute_list('id') for x in htmlPart.find_all('a', {"id": True})]
    for i in range(len(linkPart)):
        sector_elements.extend(linkPart[i])
    # print(linkPart)
    # print(sector_elements)
    # print(len(sector_elements))

    # sector_list
    sector = html.find_all('strong')
    for i in sector:
        sector_list.append(i.text.strip(':'))
        # print(i.text)
    # print(sector_list)

    # sector_name_list
    sector_n = html.select('div.text a')
    for i in sector_n:
        sector_name_list.append(i.text)
    # print(sector_name_list)

    return


def get_company_names():
    for l in sector_list:
        for e, n in zip(sector_elements, sector_name_list):
            if l.lower()[0] == e[0]:
                # set up browser
                chrome_options = webdriver.ChromeOptions()
                prefs = {"profile.managed_default_content_settings.images": 2}
                chrome_options.add_experimental_option("prefs", prefs)
                browser = webdriver.Chrome(wd,options=chrome_options)
                # browser = webdriver.Chrome() # open web page
                browser.implicitly_wait(10)  # wait for web page to load

                url_s = 'https://www.thestar.com.my/business/marketwatch/stock-list/?sector=' + e
                # sector_links.append(url_s)
                browser.get(url_s)
                name_list = browser.find_elements_by_xpath(
                    '//table[@class="market-trans"]//tr[@class="linedlist"]/td/a')
                for name in name_list:
                    if name.text != '':
                        name_text = name.text.replace("&", "%26")
                        company_names.append(name_text)
                        sector_1_list.append(l)
                        sector_2_list.append(n)
                browser.close()

    # save as links for crawling all the information
    for n in company_names:
        link = 'https://www.thestar.com.my/business/marketwatch/stocks/?qcounter=' + n
        company_links.append(link)

    return


def save_dataframe():
    na = name_list
    co = code_list
    s1 = sector_1_list
    s2 = sector_2_list

    dataframe = pd.DataFrame({'name': na, 'code': co, 'Sector_main': s1, 'sector': s2})

    # save data
    dataframe.to_csv("Day_16_sector.csv", index=False, sep=',')


class AppCrawler:
    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.apps = []

    def crawl(self):
        self.get_app_from_link(self.starting_url)
        return

    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)

        name = tree.xpath('//h1[@class="stock-profile f16"]/text()')[0]
        code = tree.xpath('//li[@class="f14"]/text()')[1]

        name_list.append(name)
        print(name)
        code_list.append(code[3:])
        print(code[3:])

        return


class App:

    def __init__(self, name, code, links):
        self.name = name
        self.code = code
        self.links = links

    def __str__(self):
        return ("Name: " + self.name.encode('UTF-8') +
                "\r\nCode: " + self.developer.encode('UTF-8') + "\r\n")


get_sectors()
get_company_names()

for link_c in company_links:
    crawler = AppCrawler(link_c, 0)
    crawler.crawl()

save_dataframe()