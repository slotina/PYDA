#!/usr/bin/env python
# coding: utf-8

# In[99]:


#1
f=open('purchase_log.txt','r',encoding='utf-8')
import json


# In[100]:


purchases={}
for line in f:
    line=json.loads(line)
    user_id=list(line.values())[0]
    category=list(line.values())[1]   
    purchases[user_id] = category
purchases


# In[116]:


purchases.get('3f8e1ccd3f')+' g'


# In[143]:


#2
g=open('visit_log.csv','r',encoding='utf-8')
fu=open('funnel.csv', 'w')


# In[144]:


for line in g:
        line=line.strip().split(',')
        if line[0] in purchases.keys():
            line.append(purchases[line[0]])
            add_line=','.join(line)
            fu.write(add_line+'\n')
        elif line[0]=='user_id':
            line.append('category')
            add_line=','.join(line)
            fu.write(add_line+'\n')
        else:
            add_line=','.join(line)

