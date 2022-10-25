#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import jinja2

### Read and clean data
#%%
#year of collection 2020
df = pd.read_csv('SA_Aqar.csv')
df.info()

#%% Check for duplicates
df[~df.duplicated()]

#%% Check for missing values
df.isnull().sum()

#%% Drop details column
df.drop('details', axis=1, inplace=True)

#%% trim the spaces in the columns names
df.columns = df.columns.str.strip()

#%% trim the spaces in the column values
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

#%% describe price including outliers
df['price'].describe(percentiles=[.25, .5, .75, .90, .95, .99]).apply(lambda x: format(x, 'f'))

#%% Sort by price and get the top 5
df.sort_values(by='price', ascending=False).head()

#%% Get count of values above the 99th percentile in price
df[df['price'] > 300000].count()

#%% describe size including outliers
df['size'].describe(percentiles=[.25, .5, .75, .90, .95, .99]).apply(lambda x: format(x, 'f'))

#%% Sort by size and get the top 5
df.sort_values(by='size', ascending=False).head()

#%% Get count of values above the 99th percentile in size
df[df['size'] > 1000].count()

#%% Unique values in front
list(df['front'].unique())
df['front'].value_counts()
#%%
df.sample(10)
#%% Style the price and size columns to use commas
df.style.format({'price': '{:,d}', 'size': '{:,d}'})

#%% Plot a histogram for the price
plt.hist(df['price'], bins=5)

#%% Get bins for price column
# bins = [1000,55000,70000,100000,17000]#[0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000, 2100000, 2200000, 2300000, 2400000, 2500000, 2600000, 2700000, 2800000, 2900000, 3000000, 3100000, 3200000, 3300000, 3400000, 3500000, 3600000, 3700000, 3800000, 3900000, 4000000, 4100000, 4200000, 4300000, 4400000, 4500000, 4600000, 4700000, 4800000, 4900000, 5000000, 5100000, 5200000, 5300000, 5400000, 5500000, 5600000, 5700000, 5800000, 5900000, 6000000, 6100000, 6200000, 6300000, 6400000, 6500000, 6600000, 6700000, 6800000, 6900000, 7000000, 7100000, 7200000, 7300000, 7400000, 7500000, 7600000, 7700000, 7800000, 7900000, 8000000, 8100000, 8200000, 8300000, 8400000, 8500000, 8600000, 8700000, 8800000, 8900000, 9000000, 9100000, 9200000, 9300000, 9400000, 9500000, 9600000, 9700000, 9800000, 9900000, 10000000, 10100000]
pd.cut(df['price'], bins=10).value_counts()

#%%
df['price'].sample(5)

#%% Get the values that are equal in price and size
df[df['price'] == df['size']]

#%% Remove the rows that have the same value in price and size
df = df[df['price'] != df['size']]

# %% Unique values in property age
uniqueAge = list(df['property_age'].unique())
uniqueAge.sort()
uniqueAge
#%% Check for properties with an elevator in each city
df[df['elevator'] == 1].groupby('city')['elevator'].count()

#%% 