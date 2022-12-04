#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


rat = pd.read_csv('ratings.csv',sep=',')
rat.head()


# In[58]:


#1 cпособ
def top (row):
    if row['rating']<=2.0:
        a='низкий'
    elif row['rating']<=4.0:
        a='средний'
    else:
        a='высокий'
    return a


# In[59]:


rat['topp']=rat.apply(top,axis=1)
rat.head()


# In[71]:


#2 cпособ
def tt(r):
    if r<=2.0:
        a='низкий'
    elif r<=4.0:
        a='средний'
    else:
        a='высокий'
    return a   


# In[72]:


rat['toppp']=rat['rating'].apply(tt)
rat.head()


# In[73]:


#2 задача


# In[75]:


geo_data = {
'Центр': ['москва', 'тула', 'ярославль'],

'Северо-Запад': ['петербург', 'псков', 'мурманск'],

'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}
geo_data


# In[77]:


keywords = pd.read_csv('keywords.csv',sep=',')
keywords.head()


# In[79]:


towns=[]
for values in geo_data.values():
    for i in values:
        towns.append(i)
towns


# In[80]:


def region_in_keyword(row):
    data=row['keyword'].split(' ')
    i=0
    for word in data:
        if word in towns:
            for items in geo_data.items():
                if word in items[1]:
                    i+=1
                    return items[0]
    if i==0:
        return 'undefined'


# In[82]:


keywords['region'] =keywords.apply(region_in_keyword, axis=1)
keywords.head()


# In[ ]:




