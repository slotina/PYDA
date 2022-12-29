#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


log = pd.read_csv('visit_log2.csv', sep=';')
log.head()


# In[ ]:


Задание 1
Для датафрейма log из материалов занятия создайте столбец source_type по правилам:

если источник traffic_source равен Yandex или Google, то в source_type ставится organic;
для источников paid и email из России ставим ad;
для источников paid и email не из России ставим other;
все остальные варианты берём из traffic_source без изменений.


# In[29]:


log.loc[log.traffic_source =='yandex', 'source_type' ] = 'organic'
log.loc[log.traffic_source =='google', 'source_type' ] = 'organic'
log.loc[((log.traffic_source == 'paid') | (log.traffic_source == 'email')) & (log.region=='Russia'), 'source_type'] = 'ad'
log.loc[((log.traffic_source == 'paid') | (log.traffic_source == 'email')) & (log.region!='Russia'), 'source_type'] = 'other'
log.head(10)


# In[ ]:





# In[31]:


import pandas as pd
import re
urls=pd.read_csv('URLs.txt')
urls[urls.url.str.contains('/[0-9]{8}-', regex=True)].head()


# In[3]:


#3
ratings = pd.read_csv('ratingss_дз продвинутый пандас.csv', sep=',')
ratings


# In[5]:


ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')
ratings.head()


# In[14]:


ratings['userId'].value_counts().loc[lambda x : x > 100]


# In[15]:


ratings_pivot_table = ratings.groupby('userId').agg({'timestamp': ['min', 'max', 'count']})['timestamp'].sort_values('count', ascending=False)


# In[16]:


ratings_pivot_table


# In[20]:


time_pivot_table = ratings_pivot_table.loc[ratings_pivot_table['count'] > 100, 'lifetime'] = (ratings_pivot_table['max'] - ratings_pivot_table['min']).mean()


# In[21]:


time_pivot_table


# In[22]:


#4
rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
rzd


# In[23]:


auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
auto


# In[24]:


air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
air


# In[25]:


client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1', 
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)
client_base


# In[26]:


all_revenue_base = client_base[['client_id']].merge(rzd, how='left', on='client_id').merge(auto, how='left', on='client_id').merge(air, how='left', on='client_id')
all_revenue_base


# In[27]:


revenue_base_all_adr = client_base.merge(rzd, how='left', on='client_id').merge(auto, how='left', on='client_id').merge(air, how='left', on='client_id'),
revenue_base_all_adr


# In[ ]:




