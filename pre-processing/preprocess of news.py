# -*- coding: utf-8 -*-

import pandas as pd
import re

##please write the path of this folder
path = "__________________________/pre-processing/"

#load data
a = pd.read_csv(path+"news/news_20190318.csv")
b = pd.read_csv(path+"news/news_20190327.csv")
c = pd.read_csv(path+"news/news_20190403.csv")
d = pd.read_csv(path+"news/news_20190410.csv")
e = pd.read_csv(path+"news/news_20190417.csv")

#merge data by columns
merge_news = a.append(b)
merge_news = merge_news.append(c)
merge_news = merge_news.append(d)
merge_news = merge_news.append(e)

#remove duplicates of news
merge_news['extract_code'] = merge_news['code'].str[-4:]
news = merge_news.sort_values('extract_code',ascending=True).drop_duplicates(['news'],keep='first')

#extract date
news['extracted_date']=news.date.str.extract(r'(\d{2}\s[A-Z][a-z]{2},\s\d{4})')

#remove news that before 25 Feb 2019
news['extracted_date']=pd.to_datetime(news['extracted_date'])
res = news[~(news['extracted_date']<'25 Feb, 2019')]

res.to_csv("appended_news.csv")
