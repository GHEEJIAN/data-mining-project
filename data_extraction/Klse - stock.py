# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:32:11 2019

@author: user
"""
#make sure selenium is installed via cmd
#make sure chromedriver is installed in the machine

#write down the location of chromedriver
wd = '________________/chromedriver'

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Referer':'https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-2305666475781689&output=html&h=90&slotname=9390552809&adk=3116781417&adf=1662620477&w=970&lmt=1552753083&guci=2.2.0.0.2.2.0.0&format=970x90&url=http%3A%2F%2Fwww.investalks.com%2Fforum%2Fforum.php%3Fmod%3Dforumdisplay%26fid%3D7%26filter%3Dtypeid%26typeid%3D17&flash=0&wgl=1&dt=1552753083912&bpp=42&bdt=108&fdt=46&idt=22&shv=r20190313&cbv=r20190131&saldr=aa&abxe=1&correlator=6683659723222&frm=20&pv=2&ga_vid=691979923.1552569252&ga_sid=1552752744&ga_hid=1232295072&ga_fc=1&iag=0&icsg=12206&dssz=10&mdo=0&mso=0&u_tz=480&u_his=3&u_java=0&u_h=864&u_w=1536&u_ah=824&u_aw=1536&u_cd=24&u_nplug=3&u_nmime=4&adx=34&ady=100&biw=1026&bih=350&scr_x=0&scr_y=0&eid=21060853&oid=3&rx=0&eae=0&fc=656&brdim=426%2C33%2C426%2C33%2C1536%2C0%2C1057%2C735%2C1042%2C350&vis=1&rsz=%7C%7CeE%7C&abl=CS&ppjl=f&pfx=0&fu=16&bc=7&ifi=1&uci=1.afatrway4czq&fsb=1&xpc=kkAgITwzNl&p=http%3A//www.investalks.com&dtd=90'}

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

page = requests.get('https://www.klsescreener.com/v2/financial-reports',headers=header)
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
