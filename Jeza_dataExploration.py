#%%
# Import necessary libraries
from statistics import mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from dataCleaning import clean

#%%
# Reading and clean the data
df = pd.read_csv("SA_Aqar.csv")
# clean(df)
# 1. Details column has missing data and is made up of unstructured data
# We will drop it
df.drop('details', axis=1, inplace=True)

# 2. Do we have any duplicates?
# First clean whitespace to be able to compare values
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
# Clean column names as well
df.columns = df.columns.str.strip()
# Remove duplicates
df = df[~df.duplicated()]
# 3. Remove the rows that have the same value in price and size
df = df[df['price'] != df['size']]
# 4. Remove fronts that are equal to '3 شوارع'
df = df[df['front'] != '3 شوارع']
# 5. Remove fronts that are equal to '4 شوارع'
df = df[df['front'] != '4 شوارع']
# 6. Remove values with a size < 100
df = df[df['size'] > 100]
# 7. Price periods are not consistent, we made an assumption that they are monthly
# 7.1 Discard anything less than 2K
df = df[df['price'] > 2000]
# 7.2 Anything beyond 20K is yearly and will be divided by 12
df['price'] = np.where(df['price'] > 20000, df['price']//12, df['price'])

#%%
df.city.groupby("district").value_counts()
#%% Plot the price mean per city
mean_per_city = df.groupby("city")["price"].mean().reset_index()
px.bar(mean_per_city, x="city", y="price", title="Mean price per city")


#%% Plot the price mean per district in Riyadh
riyadhDf = df[df["city"] == "الرياض"]
mean_district_riyadh = riyadhDf.groupby("district")\
    .agg({"price": "mean"}).reset_index()\
        .sort_values("price", ascending=False).head(5)
px.bar(mean_district_riyadh, x="district", y="price", title="Mean price per district in Riyadh")

#%% Plot the price mean per district in Jeddah
jeddahDf = df[df["city"] == "جدة"]
mean_district_jeddah = jeddahDf.groupby("district")\
    .agg({"price": "mean"}).reset_index()\
        .sort_values("price", ascending=False).head(5)
px.bar(mean_district_jeddah, x="district", y="price", title="Mean price per district in Jeddah")

#%% Plot the price mean per district in Khobar
khobarDf = df[df["city"] == "الخبر"]
mean_district_khobar = khobarDf.groupby("district")\
    .agg({"price": "mean"}).reset_index()\
        .sort_values("price", ascending=False).head(5)
px.bar(mean_district_khobar, x="district", y="price", title="Mean price per district in Khobar")

#%% Plot the price mean per district in Dammam
dammamDf = df[df["city"] == "الدمام"]
mean_district_dammam = dammamDf.groupby("district")\
    .agg({"price": "mean"}).reset_index()\
        .sort_values("price", ascending=False).head(5)
px.bar(mean_district_dammam, x="district", y="price", title="Mean price per district in Dammam")

#%% Mean per living room
mean_per_living_room = df.groupby("livingrooms")["price"].mean().reset_index()
px.bar(mean_per_living_room, x="livingrooms", y="price", title="Mean price per # of living rooms")

#%% Mean per bathrooms
mean_per_bathrooms = df.groupby("bathrooms")["price"].mean().reset_index()
px.bar(mean_per_bathrooms, x="bathrooms", y="price", title="Mean price per # of bathrooms")


#%%
##  Check livingrooms vs price
sns.set_theme()
# sns.set_context("poster")
sns.barplot(data=df, x="livingrooms", y="price", color="0.4", ci=None)
plt.title(("livingrooms VS prices"))
plt.xlabel(("livingrooms"))
plt.ylabel(("Average prices"))
#%%
# Check livingrooms vs price
sns.set_theme()
sns.barplot(data=df, x="bathrooms", y="price", color="0.4", ci=None)
plt.title(("bathrooms VS prices"))
plt.xlabel(("bathrooms"))
plt.ylabel(("Average prices"))
# %%
# count the number of properties with some features in each city
sns.set_theme()
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
# `livingrooms > 2`
data_city = df[df["livingrooms"] > 2]
sns.histplot(ax=ax1, x=arabic_plot(data_city["city"]), color="0.4")
# `driver_room == 1`
data_driver_room = df[df["driver_room"] == 1]
sns.histplot(ax=ax2, x=arabic_plot(data_driver_room["city"]), color="0.4")
# `basement == 1`
data_basement = df[df["basement"] == 1]
sns.histplot(ax=ax3, x=arabic_plot(data_basement["city"]), color="0.4")
# `elevator == 1`
data_elevator = df[df["elevator"] == 1]
sns.histplot(ax=ax4, x=arabic_plot(data_elevator["city"]), color="0.4")
ax1.set_title("Number of properties with more than two Livingrooms")
ax2.set_title("Number of properties with Driver room")
ax3.set_title("Number of properties with Basement")
ax4.set_title("Number of properties with Elevator")
ax1.set_ylabel("Count")
ax2.set_ylabel("Count")
ax3.set_ylabel("Count")
ax4.set_ylabel("Count")

#%%
sns.set_theme()
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
# `fireplace`
data_city = df[df["fireplace"] == 1]
sns.histplot(ax=ax1, x=arabic_plot(data_city["city"]), color="0.4")
# `garage`
data_driver_room = df[df["garage"] == 1]
sns.histplot(ax=ax2, x=arabic_plot(data_driver_room["city"]), color="0.4")
# `pool`
data_basement = df[df["pool"] == 1]
sns.histplot(ax=ax3, x=arabic_plot(data_basement["city"]), color="0.4")
# `bathrooms >3 `
data_elevator = df[df["bathrooms"] > 3]
sns.histplot(ax=ax4, x=arabic_plot(data_elevator["city"]), color="0.4")
ax1.set_title("Number of properties with fireplace")
ax2.set_title("Number of properties with garage")
ax3.set_title("Number of properties with pool")
ax4.set_title("Number of properties with more than three bathrooms")
ax1.set_ylabel("Count")
ax2.set_ylabel("Count")
ax3.set_ylabel("Count")
ax4.set_ylabel("Count")
#%%
# Investigating prices with and without some features
# driver_room`
sns.set_theme()
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
ax1 = sns.barplot(ax=ax1, y=df["price"], x=df["driver_room"], data=df, ci=None)
ax1.set_xlabel("")
labels = [item.get_text() for item in ax1.get_xticklabels()]
labels[0] = "Without Driver Room"
labels[1] = "With Driver Room"
ax1.set_xticklabels(labels)
ax1.set_ylabel("Price")

# ac
ax2 = sns.barplot(ax=ax2, y=df["price"], x=df["ac"], data=df, ci=None)
ax2.set_xlabel("")
labels = [item.get_text() for item in ax2.get_xticklabels()]
labels[0] = "Without AC"
labels[1] = "With AC"
ax2.set_xticklabels(labels)
ax2.set_ylabel("Price")

# pool
ax3 = sns.barplot(ax=ax3, y=df["price"], x=df["pool"], data=df, ci=None)
ax3.set_xlabel("")
labels = [item.get_text() for item in ax3.get_xticklabels()]
labels[0] = "Without Pool"
labels[1] = "With Pool"
ax3.set_xticklabels(labels)
ax3.set_ylabel("Price")

# basement
ax4 = sns.barplot(ax=ax4, y=df["price"], x=df["basement"], data=df, ci=None)
ax4.set_xlabel("")
labels = [item.get_text() for item in ax4.get_xticklabels()]
labels[0] = "Without Basement"
labels[1] = "With Basement"
ax4.set_xticklabels(labels)
ax4.set_ylabel("Price")

#%%
# check which front is the most expensive in each city
sns.set_theme()
plt.subplots(figsize=(10, 7))
sns.barplot(y="price", x=arabic_plot(ny["front"]), data=ny, color="0.4", ci=None)
plt.title(("Rental prices based on front in Riyadh"))
#%%
plt.subplots(figsize=(10, 7))
sns.barplot(y="price", x=arabic_plot(nj["front"]), data=nj, color="0.4", ci=None)
plt.title(("Rental prices based on front in Jeddah"))
#%%
plt.subplots(figsize=(10, 7))
sns.barplot(y="price", x=arabic_plot(nd["front"]), data=nd, color="0.4", ci=None)
plt.title(("Rental prices based on front in Dammam"))
#%%
plt.subplots(figsize=(10, 7))
sns.barplot(y="price", x=arabic_plot(nk["front"]), data=nk, color="0.4", ci=None)
plt.title(("Rental prices based on front in Khobar"))
