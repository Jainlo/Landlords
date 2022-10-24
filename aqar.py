#%%
import pandas as pd
import numpy as np

#%%
df = pd.read_csv('SA_Aqar.csv')
df.info()

#%%
df

#%% Check for missing values
df.isnull().sum()

#%% Drop details column
df.drop('details', axis=1, inplace=True)

#%% Check for duplicates
df[~df.duplicated()]

#%% Mean per city

#%%
df.sample(5)

#%% The majority of type of units in each city

#%% Average price per district

#%% Relationship between Price and features

#%% What type of rental units have the highest rent value.
