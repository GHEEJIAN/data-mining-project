rm(list=ls())
gc()

#make sure all the packages are installed
#write down the path
path = "___________________________________/sentiment analysis/"
library(tidyr)
library(dplyr)
#library(tidyverse)
#library(tidytext)
library(tm)
#corpus
library(stringr)
library(wordcloud)
library(syuzhet)
library(textstem)

#lemmitization

nt<-read.csv(paste0(path,"appended_news.csv"))

df2<-nt
df2$news <- gsub("http\\S+","",df2$news)

df2$news <- gsub("#\\S+","",df2$news)

df2$news <- gsub("@\\S+","",df2$news)

df2$news<- gsub("[<].+[>]", "", df2$news)
#remove unicode
df2$news <- gsub("[[:punct:]]+", " ", df2$news)

df2$news<- gsub("[[:space:]]+", " ", df2$news)

df2$news<- str_replace_all(df2$news,"'s","")
df2$news<- str_trim(df2$news)
df2$news<- gsub("[^0-9A-Za-z///' ]", "", df2$news)
#remove special characters
df2$news<-gsub('[0-9]+', '', df2$news)
df2 <-df2[!duplicated(df2$news),]
df2$news <- tolower(df2$news)

corpus <- Corpus(VectorSource(df2$news))
newstopwords<-c(stopwords("en"),"will","just","say","now","the","really","how","what","why","and","because","najib","najibs","razak")
corpus <- tm_map(corpus,removeWords,newstopwords)
corpus <- tm_map(corpus, lemmatize_strings)


DTM <- DocumentTermMatrix(corpus)
tweetsSparse <- as.data.frame(as.matrix(DTM))
