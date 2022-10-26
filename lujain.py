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
import dataCleaning
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import arabic_reshaper
from dataprep.eda import create_report


#%%Run and clean the data
df = pd.read_csv('SA_Aqar.csv')
dataCleaning.clean(df)

######------DATA EXPLORATION------######
#%% general information
df.info()

#%% Column names
df.columns

#%% automated report
create_report(df)


#%% Q4. Price periods are different, so we need to make an assumption
# We will assume that they're monthly rent
# All rentals that start at 2K and end at 20K are monthly
# Anything beyond that will be divided by 12
# Anything less will be dropped
#------
prices = sorted(set(df['price']))
# Original data starts at 1K
# Ends at 1.7M

# discard anything less than 2K
df = df[df['price'] > 2000] 
# Divide prices over 20K by 12
#%%
df2['price'] = np.where(df2['price'] > 20000, df2['price']/12, df2['price'])
# round up
sorted(set(df2['price']))



#%% Interesting variables
# Price vs
# Property age vs
# Pool with Price
# Pool with size
# Pool with city

######Questions######
# Is there a perferred front?
# Is there a front that is more expensive?
# Which cities tend to have more pools? Could there be a reason?
# Whats the average price per district
# Are there cities with more driver_rooms
# Are there cities with more basements? Could there be a reason?

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



#%% 
import arabic_reshaper
from bidi.algorithm import get_display

sns.set_theme(style="whitegrid")

def arabic_plot(labels: pd.Series):
    ArabicLabels = labels.apply(arabic_reshaper.reshape)
    result = []
    for label in ArabicLabels:
        result.append(get_display(label))
    if len(result) == 1:
        return result[0]
    else:
        return result

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 8))

# total - total city count
# abbrev - city
# alcohol - pool sum

# Plot the the size
sns.set_color_codes("pastel")
# x is total per city
sns.barplot(x=df.groupby('city').count(), y=df.groupby('city').sum(), data=df,
            label="size", color="b")
# Plot the houses that have pools
sns.set_color_codes("muted")
sns.barplot(x="pool", y=arabic_plot(df["city"]), data=df,
            label="Pool included", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(ylabel="city",
       xlabel="size")
sns.despine(left=True, bottom=True)

# %%
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# Load the example car crash dataset
crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)

# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="total", y="abbrev", data=crashes,
            label="Total", color="b")

# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="alcohol", y="abbrev", data=crashes,
            label="Alcohol-involved", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="Automobile collisions per billion miles")
sns.despine(left=True, bottom=True)

# %%
# How many have a pool
df.groupby('city').sum()
# How many houses in each city
df.groupby('city').count()