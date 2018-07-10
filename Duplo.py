
# coding: utf-8

# In[2]:


#This code uses a lego database to find out how many lego pieces you have
#In addition, it scrapes the original MSRP (in USD), and plots the cost per piece of your sets
#Note, you need to download the database
#https://www.kaggle.com/rtatman/lego-database
import pandas as pd

#List your sets here
sets=pd.Series(['10532-1','10590-1','10583-1','10567-1','10615-1','10528-1','10600-1','10570-1','10819-1','10617-1','10599-1','10818-1','10577-1','10813-1','10808-1','10580-1','10811-1','4962-1'],name='sets')


# In[3]:


df=pd.read_csv('/Users/ed/Downloads/lego-database/sets.csv') #Point this to where you saved the database


# In[4]:


df.head()


# In[5]:


sets=pd.Series(['10532-1','10590-1','10583-1','10567-1','10615-1','10528-1','10600-1','10570-1','10819-1','10617-1','10599-1','10818-1','10577-1','10813-1','10808-1','10580-1','10811-1','4962-1'],name='sets')
Mysets=df[df.set_num.isin(sets)]
Mysets


# In[6]:


Mysets.num_parts.sum()


# In[7]:


#Mysets.price[Mysets.set_num[sets[0]]=1


# In[8]:


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


# In[9]:


Mysets['price2'] = Mysets['price2'].apply(pd.to_numeric)


# In[10]:


Mysets.price2.sum()


# In[11]:


import numpy as np
import matplotlib.pyplot as plt


# In[13]:


plt.scatter(Mysets.num_parts,Mysets.price2,)
plt.xlabel("Pieces")
plt.ylabel("USD")
plt.title("Duplo Price Per Piece")


# In[ ]:



