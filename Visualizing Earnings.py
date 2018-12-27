#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


recent_grads = pd.read_csv('recent-grads.csv')
recent_grads.shape


# In[4]:


recent_grads.head()
recent_grads.tail()


# In[9]:


recent_grads.iloc[0]


# In[20]:


recent_grads.describe()


# In[22]:


raw_data_count = recent_grads.shape[0]


# In[23]:


recent_grads.dropna()


# In[25]:


clean_data_count = recent_grads.shape[0]


# In[27]:


recent_grads.plot(x='Sample_size',y='Median',kind='scatter')


# In[28]:


recent_grads.plot(x='Sample_size',y='Unemployment_rate',kind='scatter')


# In[29]:


recent_grads.plot(x='Full_time',y='Median',kind='scatter')


# In[30]:


recent_grads.plot(x='ShareWomen',y='Unemployment_rate',kind='scatter')


# In[31]:


recent_grads.plot(x='Men',y='Median',kind='scatter')


# In[32]:


recent_grads.plot(x='Women',y='Median',kind='scatter')


# In[42]:


import numpy as py
get_ipython().magic('matplotlib inline')
dudes = recent_grads[recent_grads['ShareWomen'] < .5]['Median']

plt.hist(dudes)


# In[43]:


recent_grads['Sample_size'].hist()


# In[45]:


recent_grads['Median'].hist()


# In[48]:


recent_grads['Employed'].hist(bins=10,range=(0,60000))


# In[50]:


recent_grads['Full_time'].hist(range=(0,50000))


# In[57]:


recent_grads['ShareWomen'].hist()
recent_grads[recent_grads['ShareWomen'] > .5]['ShareWomen'].hist()


# In[53]:


recent_grads['Unemployment_rate'].hist()


# In[54]:


recent_grads['Men'].plot(kind='hist')


# In[55]:


recent_grads['Women'].hist()


# In[59]:


from pandas.plotting import scatter_matrix


# In[60]:


scatter_matrix(recent_grads[['Sample_size','Median']],figsize=(10,10))


# In[61]:


scatter_matrix(recent_grads[['Sample_size','Median','Unemployment_rate']],figsize=(8,8))


# In[68]:


recent_grads[:10].plot.bar(x='Major',y='ShareWomen',legend=False)
recent_grads[len(recent_grads)-10:].plot.bar(x='Major',y='ShareWomen',legend=False)


# In[ ]:




