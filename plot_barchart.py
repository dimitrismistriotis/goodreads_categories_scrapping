
# coding: utf-8

# In[2]:

get_ipython().magic('matplotlib inline')


# In[3]:

get_ipython().magic('matplotlib inline')


# In[4]:

import math as math


# In[5]:

import matplotlib.pyplot as plt


# In[6]:

#import numpy as np
import pandas as pd


# In[7]:

data = pd.Series({'cat1': 8200000, 'cat2': 6800123, 'cat3': 7800000, 'cat4': 6000000,
                 'cat5': 4300000, 'cat6': 4100000, 'cat7': 3800000, 'cat8': 3500000,
                 'cat9': 3400000, 'cat10': 3300000})
data


# In[8]:

data.plot(kind='barh', color='k')


# Very nice up to here, but not what I want...

# In[9]:

dataf = pd.DataFrame(data, columns=['books_published'])
dataf


# In[10]:

max_value = dataf.max()['books_published']
annotation_divisior = 10 ** (math.floor(math.log(max_value, 10)))

dataf['color'] = '#afafaf'
dataf.loc[dataf['books_published'] == max_value, ['color']] = '#f70e0e'
#dataf.loc[dataf['books_published'] != max_value, ['color']] = '#afafaf'
dataf


# In[11]:

dataf = dataf.sort_values(['books_published'], ascending=[True])
dataf


# 
# Stack Overflow to the rescue for annotating(!):
# http://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns

# In[21]:

ax = dataf.plot(kind='barh', legend=False,
                  color=[dataf['color']],
                  linestyle=None,
                  # title="Books published per category",
                  figsize=(15, 10), fontsize=20)

for p in ax.patches:
    ax.annotate("%.1f" % (p.get_width() / annotation_divisior),
                (p.get_x() + p.get_width(), p.get_y()), xytext=(5, 10),
                textcoords='offset points', fontsize=18)


# In[22]:

fig = ax.get_figure()
fig.savefig('diagram.png')


# In[ ]:



