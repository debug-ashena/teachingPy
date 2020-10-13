#!/usr/bin/env python
# coding: utf-8

# In[1]:

Is it necessary to change this way?

import sklearn


# In[2]:


from sklearn.datasets import load_breast_cancer


# ## load_dataset

# In[4]:


data=load_breast_cancer()


# ## Organize our data

# In[5]:


label_names=data['target_names']


# In[6]:


labels=data['target']


# In[7]:


feature_names=data['feature_names']


# In[8]:


features=data['data']


# ## Look at our data

# In[16]:


print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])


# In[17]:


from sklearn.model_selection import train_test_split


# ## Split Our Data

# In[18]:


train, test, train_labels, test_labels=train_test_split(features,labels,test_size=0.33 , random_state=42)


# In[20]:


from sklearn.naive_bayes import GaussianNB


# ## Initialize our classifier

# In[25]:


gnb=GaussianNB()


## Train our cliassifier

model=gnb.fit(train, train_labels)


# 

# ## Make predictions

# In[26]:


pred=gnb.predict(test)
print(pred)


# In[27]:


from sklearn.metrics import accuracy_score


# ## Evaluate accuracy

# In[28]:


print(accuracy_score(test_labels, pred))


# In[ ]:




