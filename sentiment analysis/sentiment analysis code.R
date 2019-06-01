#make sure all the packages are installed

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


wordcloud(corpus ,min.freq=20,scale=c(1.1,0.28),colors=brewer.pal(8, "Dark2"),random.color= FALSE, random.order = FALSE, max.words = 300)

sentiscore<-get_sentiment(df2$news,method="bing")

df3<-cbind(df2,sentiscore)
df3<-df3%>%
  mutate(final_sentiment=ifelse(sentiscore>0,"pos",ifelse(sentiscore<0,"neg","neu")))
write.csv(df3,"news_with_sentiment.csv",row.names = FALSE)
