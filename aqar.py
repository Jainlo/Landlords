#%%
import pandas as pd
import numpy as np
import seaborn as sns
import dataprep.eda as dp

### Read and clean data
#%%
#year of collection 2020
df = pd.read_csv('SA_Aqar.csv')
df.info()

#%%
df

#%% Create dataprep report
report = dp.create_report(df)
report.save('report.html')

#%% Check for missing values
df.isnull().sum()

#%% Drop details column
df.drop('details', axis=1, inplace=True)

#%% trim the spaces in the columns names
df.columns = df.columns.str.strip()

#%% trim the spaces in the column values
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

#%% Check for unique values in city column
df['city'].unique()
len(df['city'].unique())

#%% Filer unique districts by city
df[df["city"] == "الرياض"]
# jeddah = df.query('city == "الرياض"')
# jeddah

#%% Check for duplicates
df[~df.duplicated()]

# Exploratory Data Analysis

#%% Use the describe method to get the summary statistics of the data
df.describe()

#%% Describe by city
df.groupby('city').describe()

#%% Mean per city
df.groupby('city')["price"].mean()

#%%
df.groupby('city')['price'].describe()
#%%
df.sample(5)

#%% Do we have outliers in the dataset?
ry_prices = df[(df["city"] == "الرياض") & (df['district'])]
sns.boxplot(ry_prices, x= "district", y= "price")
#arabic words in plot (?)
#jeddah has outliers in prices, why ?
#%%
ry_prices.describe()
#%%
sns.boxplot(df[df["city"] == "الرياض"], x= "city", y= "size")

#%% The majority of type of units in each city

#%% Average price per district

#%% Relationship between Price and features

#%% What type of rental units have the highest rent value.

#%% Compare mean price of properties with all featers per city
df[(df["garage"] == 1) & (df["elevator"] == 1) & (df["pool"] == 1)   & (df["basement"] == 1) & (df["frontyard"] ==  1) & (df["ac"] == 1)].groupby('city')['price'].mean()
