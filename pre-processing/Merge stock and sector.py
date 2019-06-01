import pandas as pd
import os

##please write the path of this data mining project located
path = "_______________________________/pre-processing/"

def price_csv():
    df_list = []
    
    SaveFile_Name = r'35_days_price.csv'
    file_list = os.listdir(path+'Price_csv')
    file_list.sort(key=lambda x:int(x[4:-4]))
    
    #Loop through the names of the individual CSV files in the list and append them to the merged file
    for i in range(0,len(file_list)):
        df = pd.read_csv(path+'Price_csv/' + file_list[i])
        df_list.append(df)
    
    df = pd.concat(df_list)
    df.to_csv(SaveFile_Name,index=False,sep=',')


def sector_csv():
    df_list = []
    
    SaveFile_Name = r'35_days_sector.csv'
    file_list = os.listdir(path+'Sector_csv')
    file_list.sort(key=lambda x:int(x[4:-11]))
    
    #Loop through the names of the individual CSV files in the list and append them to the merged file
    for i in range(0,len(file_list)):
        df = pd.read_csv(path+'Sector_csv/' + file_list[i])
        df_list.append(df)
    
    df = pd.concat(df_list)
    df = df.drop_duplicates()
    df.to_csv(SaveFile_Name,index=False,sep=',')

# merge 20 days csv files
price_csv()
sector_csv()
# read csv files
price = pd.read_csv('35_days_price.csv')
sector = pd.read_csv('35_days_sector.csv')
# merge price and sector
stock = pd.merge(price, sector.drop(['code'],axis=1), on = 'name', how = 'left')
#print(stock)
stock.to_csv('Stock_35days.csv',index=False,sep=',')


