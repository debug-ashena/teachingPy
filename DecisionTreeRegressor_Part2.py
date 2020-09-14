#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


from sklearn.tree import DecisionTreeRegressor


# In[5]:


diabete_data=pd.read_csv("diabetes.csv")


# آبجکت هدف را ایجاد می کنم و نامش را target میگذارم

# In[48]:


target=pd.DataFrame(data=diabete_data.values[: ,8] , columns=["Has Diabete"])


# In[111]:


diabete_data.columns


# In[88]:


filtered_diabete_data=diabete_data.dropna(axis=0)


# In[89]:


y=filtered_diabete_data.Outcome


# In[112]:


diabete_features=["Pregnancies" ,"Glucose" ,"SkinThickness","Insulin","DiabetesPedigreeFunction" ,"Age"]


# In[113]:


X=filtered_diabete_data[diabete_features]


# In[114]:


diabete_model=DecisionTreeRegressor()


# In[115]:


diabete_model.fit(X,target)


# ### Cross Validation 

# In[116]:


from sklearn.metrics import mean_absolute_error


# In[117]:


predicted_diabetes=diabete_model.predict(X)


# In[118]:


mean_absolute_error(y,predicted_diabetes)


# کد قبلی محاسبه خطای میانگین برای بدست آوردن میانگین خظای پیش آمده در زمان پیشبینی است که همانطور که مشاهده می کنید دور از واقعیت است.باید ابتدا مرحله یادگیری را انجام دهیم و سپس پیش بینی و خطاها را ارزیابی کنیم.
# 

# In[119]:


from sklearn.model_selection import train_test_split


# در کد پایین می خواهم داده آموزشی و داده ولید رو از هم جدا و اسپلیت کنم

# In[120]:


train_X , Val_X , train_y , Val_y=train_test_split(X,y,random_state=0)


# در اینجا مدل رو تعیین میکنم که همان مدل درخت تصمیم است##

# In[121]:


diabete_model=DecisionTreeRegressor()


# ##Dar code paiin az attribute haye montakhab dar X , ba hadafe y olgou misazam

# In[122]:


diabete_model.fit(train_X, train_y)


# ### Get predicted diabetes on validation data

# In[123]:


Val_predictions=diabete_model.predict(Val_X)


# In[124]:


print(mean_absolute_error(Val_y, Val_predictions))

مقدار خطای میانگین بدست امده در این مرحله به واقعیت نزدیک تر است
# In[125]:


def get_mae(max_leaf_nodes, train_X , Val_X , train_y, Val_y):
    model=DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val=model.predict(Val_X)
    mae=mean_absolute_error(Val_y , preds_val)
    return(mae)


# yek Function neveshtim be esme get_mae ke magaadire mokhtalefe max_leaf_nodes ro mogaayese mikone.chera? 
# bw khaatere qaziye Overfitting va Underfitting

# In[126]:


for max_leaf_nodes in [5,50,500,5000]:
    my_mae=get_mae(max_leaf_nodes, train_X , Val_X , train_y , Val_y)
    print("MAX Leaf Nodes: %d \t\t mean_absolute_error:%d"  % (max_leaf_nodes, my_mae))


# In[127]:


candidate_max_leaf_nodes=[5, 25, 50, 100, 250, 500]


# #### Write loop to find the ideal tree size from candidate_max_leaf_nodes 
# In halge baraye peida kardane behtarin magaadire baraye max_leaf_nodes hast

# In[128]:


best_size=5
min_mae=99999


# In[129]:


for max_leaf_nodes in candidate_max_leaf_nodes:
    my_mae=get_mae(max_leaf_nodes, train_X , Val_X , train_y , Val_y)
    if my_mae< min_mae:
          min_mae=my_mae
    best_size=max_leaf_nodes


# In[130]:


best_tree_size=best_size


# In[131]:


final_model=DecisionTreeRegressor(max_leaf_nodes=best_tree_size ,random_state=1)
final_model.fit(X,y)


# In[ ]:





# In[ ]:




