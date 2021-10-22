#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#import libraries
import pandas as pd
# read our csv file
a=pd.read_csv('python_assesment .csv')
#  print our product
print(a['name'])


# In[9]:


with open ("python_assesment .csv","r") as f:
    Product=f.read().split("\n")


# In[10]:


#FuzzyWuzzy is a library of Python which is used for string matching. 
#Fuzzy string matching is the process of finding strings that match a given pattern
from fuzzywuzzy import process


# In[11]:


def get_product(query,choices=list,limit=20):
    results=process.extract(query,choices,limit=limit)
    return results


# In[12]:


get_product(input("enter a products:"),Product)

