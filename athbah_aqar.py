#%%
from ctypes import sizeof
import pandas as pd
import numpy as np
import seaborn as sns

 #%%
df = pd.read_csv('../Landlords/SA_Aqar.csv')

#%%
df.info()

#%%
df.describe()

#%%
df.isnull().sum()

#%%
df.drop('details', axis = 1, inplace =True)

#%%
df.duplicated().sum()

#%% trim the spaces in the columns names
df.columns = df.columns.str.strip()
#%% trim the spaces in the column values
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

#%%
df.city.value_counts()

#%%
df.groupby("city")["price"].mean() 

#%%
df.groupby(["city","frontyard"]).count()[['pool']]

#%%
df.groupby("city").count()['pool'].plot.bar()

#%%
df.groupby("city").count()['basement'].plot.bar()

#%%
df[df["city"] == "الرياض"]

# %%
df.groupby('city')['price'].describe()

#%% Do we have outliers in the dataset?
ry_prices = df[(df["city"] == "الرياض") & (df['district'])]
sns.boxplot(ry_prices, x= "district", y= "price")
# %%


#%%
# How many houses in each district in Riyad city”?
#len(df[(df["city"] == "الرياض") & (df['district'])])
ry_house = df[(df["city"] == "الرياض") & (df['district'])]
ry_house.district.value_counts()

#%%
#ry_house['district'].value_counts().plot(kind = 'pie', figsize =(6,6))

#%%

jd_house = df[(df["city"] == "جدة") & (df['district'])]
jd_house.district.value_counts()


#%%
dm_house = df[(df["city"] == "الدمام") & (df['district'])]
dm_house.district.value_counts()

#%%
kb_house = df[(df["city"] == "الخبر") & (df['district'])]
kb_house.district.value_counts()

#%%
# What fraction of the total do they represent?
#len(df[df.city=="الرياض"])/len(df)

# %%
#range of property_age / price? 
#ry_size = df[(df["city"] == "الخبر") & (df['district'])]
#sns.boxplot(ry_size, x= "district", y= "size")

ry_size = df[(df["city"] == "الخبر") & (df['property_age'])]
sns.boxplot(ry_size, x= "property_age", y= "price")


# %%
len(ry_house.loc[(ry_house['size'] <500)])
# %%
#ry = df[(df["city"] == "الرياض")]
#ry_compare = ry[(ry["district"] == "district") & (df['district'])]


#%%
riyadh = df[df["city"] == "جدة"]
riyadh.info()

#%%
jeddah = df[df["city"] == "جدة"]
jeddah.info()

#%%
dammam = df[df["city"] == "الدمام"]
dammam.info()

#%%
khobar = df[df["city"] == "الخبر"]
khobar.info()
#%%
# Correlation of Riyadh
riyadh.corr()

#%%
# Correlation of Jeddah
jeddah.corr()

#%%
# Correlation of Dammam
dammam.corr()

#%%
# Correlation of Khobar
khobar.corr()

#%%
riyadh.district.value_counts()

# %%
arr = ["حي العارض","حي النرجس"]

district = riyadh["district"]

for i in district:
    for j in arr:
        if i == j:
            print(True)

# %%
#riyadh["district"]
# %%
