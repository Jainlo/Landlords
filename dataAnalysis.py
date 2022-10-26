######DATASET######
# 4 cities
# n district per city (?)
# year of collection: 2020
# all are rental
# rental period differs making it hard to compare prices => make an assumption
# type of property is not included
# divide districts by direction
# set price range
# whats the size unit

#%%
from dataCleaning import clean
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.io as pio
import arabic_reshaper
from dataprep.eda import create_report


#%%Run and clean the data
df = pd.read_csv('SA_Aqar.csv')
clean(df)

######------DATA EXPLORATION------######
#%% general information
df.info()

#%% Column names
df.columns

#%% automated report
create_report(df)

#%% Interesting variables
# Price vs (?)
# Property age vs (?)
# Pool with size
# Pool with city

######Questions######
# Is there a perferred front?
# Is there a front that is more expensive?
# Which cities tend to have more pools? Could there be a reason?
# Whats the average price per district
# Are there cities with more driver_rooms
# Are there cities with more basements? Could there be a reason?
# Which city has the highest/lowest rent rate?

######Plots######
# seaborn or matplotlib or plotly
# make sure to add x labels and y labels and title
# change color palettes
# can change hue
# can change sizes
# can change figsize
# can change alpha value
# can use Horizontal bar Plots with 0 and 1 variable
# can use Smooth kernel density with marginal histograms to spot concentration of data points
# can use animation frame/ animation group

######Conclusions######
# Can we conclude that real estate has higher prices in one city more than the other three?
# Can we conclude which feature is more prominent in expensive real estate?

#%% 
# Only run this if you didnt run the dataCleaning file
# Clean the prices 2K - 80K
df = df[df['price'] > 2000] 
df['price'] = np.where(df['price'] > 20000, df['price']//12, df['price'])
df = df[df['price'] < 80000] 
# The rest of cleaning
df = df[df['size'] > 100]
df = df[~df.duplicated()]
df = df[df['price'] != df['size']]
df = df[df['front'] != '3 شوارع']
df = df[df['front'] != '4 شوارع']
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df.columns = df.columns.str.strip()
#%% 
# Q1. Which feature is more prominent in expensive real estate?
# City with the higest mean price 
df.groupby("city")["price"].mean() # highest: Jeddah, lowest: Dammam
# Most common feature in Jeddah real estate
df.groupby("city").sum()
# garage = 310 - frontyard = 311 - driver_room = 319 


# %%
# Q1. Is there a preferred front?
# Whats the most common front?
data = [dict(
  type = 'scatter',
  x = df['front'],
  y = df['front'].count(),
  mode = 'markers',
  transforms = [dict(
    type = 'groupby',
    groups = df['front'],
  )]
)]
fig_dict = dict(data=data)
pio.show(fig_dict, validate=False)

#%% This doesnt really give us useful information
# Q2. Dig deeper into شمال
# import plotly.express as px

# fig = px.scatter(df.query("front=='شمال'"), x="price", y="size",
# 	         size="size", color="city",
#                  hover_name="city", log_x=True, size_max=60)
# fig.show()

#%% 
# Q3. Is there a front that is more expensive?
# Bar plot with x = front y = price
# Explain the error bar (?)
from bidi.algorithm import get_display

def arabic_plot(labels: pd.Series):
    ArabicLabels = labels.apply(arabic_reshaper.reshape)
    result = []
    for label in ArabicLabels:
        result.append(get_display(label))
    if len(result) == 1:
        return result[0]
    else:
        return result
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(df["front"]), data=df)
plt.ylabel(arabic_plot(pd.Series("الأسعار ")))
plt.xlabel(arabic_plot(pd.Series("الواجهات")))
plt.title(arabic_plot(pd.Series(" أسعار الأجار حسب الواجهات")))

#%%
# Q4. Which cities tend to have more pools? Could there be a reason?
data = [dict(
  type = 'scatter',
  x = df['city'],
  y = df['pool'].count(),
  mode = 'markers',
  transforms = [dict(
    type = 'groupby',
    groups = df['city'],
  )]
)]
fig_dict = dict(data=data)
pio.show(fig_dict, validate=False)

# Q5. 
# %%
df.head()