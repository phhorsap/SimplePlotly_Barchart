#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# In[2]:


df = pd.read_csv('2018WinterOlympics.csv')


# In[7]:


#print(df.head())
#print(df['NOC'])
data = go.Bar(
        x= df['NOC'],
        y= df['Total'])
layout = go.Layout(
            title= 'My Chart')
fig = go.Figure(data = data, layout = layout)

pyo.plot(fig)


# In[ ]:




