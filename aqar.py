#%%
import pandas as pd
import numpy as np

# Read and clean data
#%%
df = pd.read_csv('SA_Aqar.csv')
df.info()

#%%
df

#%% Check for missing values
df.isnull().sum()

#%% Drop details column
df.drop('details', axis=1, inplace=True)

#%% trim the spaces in the columns
df.columns = df.columns.str.strip()

#%% trim the spaces in the values
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
df.groupby('city').mean()

#%%
df.sample(5)

#%% The majority of type of units in each city

#%% Average price per district

#%% Relationship between Price and features

#%% What type of rental units have the highest rent value.
