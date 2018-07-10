#This code uses a lego database to find out how many lego pieces you have
#In addition, it scrapes the original MSRP (in USD), and plots the cost per piece of your sets
#Note, you need to download the database
#https://www.kaggle.com/rtatman/lego-database
import pandas as pd

#List your sets here
sets=pd.Series(['10532-1','10590-1','10583-1','10567-1','10615-1','10528-1','10600-1','10570-1','10819-1','10617-1','10599-1','10818-1','10577-1','10813-1','10808-1','10580-1','10811-1','4962-1'],name='sets')



df=pd.read_csv('/Users/ed/Downloads/lego-database/sets.csv') #Point this to where you saved the database


df.head()

#Input set list
sets=pd.Series(['10532-1','10590-1','10583-1','10567-1','10615-1','10528-1','10600-1','10570-1','10819-1','10617-1','10599-1','10818-1','10577-1','10813-1','10808-1','10580-1','10811-1','4962-1'],name='sets')
Mysets=df[df.set_num.isin(sets)]
Mysets

#pull part totals from database
Mysets.num_parts.sum()




#Scrape price data

from bs4 import BeautifulSoup
import numpy as np
import requests
for set in sets:
    print("http://www.brickinvesting.com/lego/"+set[:-2])
    url = "http://www.brickinvesting.com/lego/"+set[:-2]
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    spans = soup.find_all('span', attrs={'itemprop':"price"})
    for span in spans:
        print (span.string)
        pric=str(span.string)
        Mysets.is_copy=False
        Mysets.loc[Mysets['set_num'].str.contains(set),'price2']=pric
        #print(set+ " " + pric)


Mysets['price2'] = Mysets['price2'].apply(pd.to_numeric)


Mysets.price2.sum()



import numpy as np
import matplotlib.pyplot as plt


#plot
plt.scatter(Mysets.num_parts,Mysets.price2,)
plt.xlabel("Pieces")
plt.ylabel("USD")
plt.title("Duplo Price Per Piece")







