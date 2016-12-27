
# coding: utf-8

# In[1]:

import pandas


# In[4]:

data = pandas.read_csv("C:\\Users\\kamalnee\\Documents\\Anaconda\\data_files\\thanksgiving-2015-poll-data.csv", encoding="Latin-1")


# In[5]:

print(data.head(5))


# In[6]:

data.info()


# In[8]:

series_data = data["Do you celebrate Thanksgiving?"]
print(series_data[:5])


# In[9]:

print(series_data.value_counts())


# In[12]:

data = data[data["Do you celebrate Thanksgiving?"]=="Yes"]
print(data.shape)


# In[14]:

series_main_dish = data["What is typically the main dish at your Thanksgiving dinner?"]
print(type(series_main_dish))
print(type(series_main_dish.value_counts()))
print(series_main_dish.value_counts())


# In[17]:

df1=data.loc[series_main_dish=="Tofurkey"]
print(df1["Do you typically have gravy?"])
print(df1.shape)


# In[26]:

apple_isnull = pandas.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
pumpkin_isnull = pandas.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
pecan_isnull = pandas.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])

ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
print(ate_pies)

print(data.loc[ate_pies==True])


# In[27]:

print(data["Age"].value_counts())


# In[40]:

def int_age(string_age):
    if(pandas.isnull(string_age)):
        return None
    elif("+" in string_age):
        return int(string_age.replace("+",""))
    else:
        age_array = string_age.split(" ")
        age=age_array[0]
        return int(age)

series_age = data["Age"]
data["int_age"]=series_age.apply(lambda x: int_age(x))
print(series_age.apply(lambda x: int_age(x)))
        


# In[ ]:




# In[34]:

def int_income(string_income):
    if pandas.isnull(string_income) or "Prefer" in string_income:
        return None
    else:
        income_list = string_income.split(" ")
        income_str = income_list[0]
        income = income_str.replace("$","").replace(",","")
        return int(income)
    
series_income = data["How much total combined money did all members of your HOUSEHOLD earn last year?"]
data["int_income"]=series_income.apply(lambda x: int_income(x))

print(data["int_income"])
        


# In[37]:

less_earning_df = data[data["int_income"] < 50000]
print(less_earning_df["How far will you travel for Thanksgiving?"].value_counts)

more_earning_data = data[data["int_income"] > 150000]
print(more_earning_data["How far will you travel for Thanksgiving?"].value_counts)


# In[41]:

df=data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", values="int_age")
print(df)


# In[ ]:




# In[ ]:



