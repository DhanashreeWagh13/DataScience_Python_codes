#!/usr/bin/env python
# coding: utf-8

# In[15]:


#INSTALLING PANDAS
get_ipython().system('pip install pandas')


# In[16]:


#IMPORTING LIBRARIES
import pandas as pd


# In[8]:


import numpy as np
import matplotlib as mpl
import seaborn as sns


# In[9]:


#IMPORTING DATASET USING PANDAS LIBRARY
df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")


# In[ ]:


###DATA FRAME DATA TYPES


# In[54]:


df.dtypes


# In[ ]:


####DATA FRAME ATTRIBUTES


# In[12]:


df.dtypes


# In[13]:


df.columns


# In[17]:


df.axes


# In[19]:


df.shape


# In[20]:


df.columns


# In[21]:


#### TO KNOW ALL THE ATTRIBUTES AND METHODS
dir(df)


# In[22]:


###### DATA FRAME METHODS


# In[23]:


df.head(10)


# In[24]:


df.tail()


# In[25]:


df.describe()


# In[26]:


df.max()


# In[27]:


df.min()


# In[28]:


df.mean()


# In[29]:


df.mode()


# In[30]:


df.median()


# In[31]:


df.std()


# In[32]:


df.sample(10)


# In[55]:


df


# In[34]:


df.dropna()


# In[35]:


#### MEAN VALUES OF FIRST 50 RECORDS IN THE DATASET 
#METHOD 1
#STEP1
df1=df.head(50)


# In[36]:


#STEP2
df1.mean()


# In[39]:


#METHOD 2
df.head(50).mean()


# In[42]:


#### TO SELECT A COLUMN IN A DATAFRAME
#METHOD 1
df["rank"]


# In[57]:


#METHOD2
df.phd


# In[45]:


#CALCULATE BASIC STATISTICS ON PHD COLUMN
#METHOD 1
df["phd"].describe()


# In[46]:


#METHOD 2
df.phd.describe()


# In[47]:


#TO FIND THE TOTAL NUMBER OF VALUES IN THE PHD COLUMN
df.phd.count()


# In[49]:


##CALCULATE AVERAGE OF PHD COLUMN
#METHOD 1
df.phd.mean()


# In[53]:


#METHOD 2
df["phd"].mean()


# In[ ]:




