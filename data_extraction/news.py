# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:59:49 2019

@author: LENOVO
"""
#make sure selenium is installed via cmd
#make sure chromedriver is installed in the machine

#write down the location of chromedriver
wd = '________________/chromedriver'

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Referer':'https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-2305666475781689&output=html&h=90&slotname=9390552809&adk=3116781417&adf=1662620477&w=970&lmt=1552753083&guci=2.2.0.0.2.2.0.0&format=970x90&url=http%3A%2F%2Fwww.investalks.com%2Fforum%2Fforum.php%3Fmod%3Dforumdisplay%26fid%3D7%26filter%3Dtypeid%26typeid%3D17&flash=0&wgl=1&dt=1552753083912&bpp=42&bdt=108&fdt=46&idt=22&shv=r20190313&cbv=r20190131&saldr=aa&abxe=1&correlator=6683659723222&frm=20&pv=2&ga_vid=691979923.1552569252&ga_sid=1552752744&ga_hid=1232295072&ga_fc=1&iag=0&icsg=12206&dssz=10&mdo=0&mso=0&u_tz=480&u_his=3&u_java=0&u_h=864&u_w=1536&u_ah=824&u_aw=1536&u_cd=24&u_nplug=3&u_nmime=4&adx=34&ady=100&biw=1026&bih=350&scr_x=0&scr_y=0&eid=21060853&oid=3&rx=0&eae=0&fc=656&brdim=426%2C33%2C426%2C33%2C1536%2C0%2C1057%2C735%2C1042%2C350&vis=1&rsz=%7C%7CeE%7C&abl=CS&ppjl=f&pfx=0&fu=16&bc=7&ifi=1&uci=1.afatrway4czq&fsb=1&xpc=kkAgITwzNl&p=http%3A//www.investalks.com&dtd=90'}

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

browser = webdriver.Chrome(wd)  # open web page
browser.implicitly_wait(10)
url='https://www.klsescreener.com/v2/'
browser.get(url)
screen_button=browser.find_element_by_id('submit')
screen_button.click()
#wait until the browser load after clicking the screen button and obtain the new web source
wait=WebDriverWait(browser,10)
element=wait.until(
            EC.presence_of_element_located((By.CLASS_NAME,"table-responsive")))
html=browser.page_source
soup = BeautifulSoup(html, "html.parser")
#print(soup.prettify())

#locate the result table
stock_table=soup.find(id="result")

#create a list for codes
links = []
for a in stock_table:
    rowsodd = stock_table.find_all(attrs={'class':'list odd'})
    rowseven = stock_table.find_all(attrs={'class':'list even'})
    for item in rowsodd:
        stock_code =item.find('td',attrs={'title':'Code'}).text
        links.append(stock_code)
    for item in rowseven:
        stock_code =item.find('td',attrs={'title':'Code'}).text
        links.append(stock_code)

#remove duplicates
mylinks = list(dict.fromkeys(links))

#add the code to form news urls
company_links = []
for n in mylinks:
    link = 'https://www.klsescreener.com/v2/news/stock/' + n
    company_links.append(link)

#extract news and respective date
df=pd.DataFrame([])
for l in company_links:
    company_news = []
    company_date=[]
    code = l
    page = requests.get(l,headers=header)
    soup = BeautifulSoup(page.text, 'html.parser')
    news_table=soup.find(id="section")
    for b in news_table.find_all('h2',{"class":"figcaption"}):
    #print(b.get_text())
        company_news.append(b.get_text())
        
    for c in news_table.find_all('div',{"class":"item-title-secondary subtitle"}):
        company_date.append(c.get_text())
    dataframe=pd.DataFrame({'code':code, 'date':company_date,'news':company_news})
    df=df.append(dataframe)
    
#save to csv
df.to_csv("news.csv",index=False,sep=',')
