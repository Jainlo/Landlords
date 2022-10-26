
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display

import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
from folium.plugins import FastMarkerCluster
#%%
df = pd.read_csv('../Landlords/SA_Aqar.csv')
df.info()
#%% Check for missing values
df.isnull().sum()
#%% Drop details column
df.drop('details', axis=1, inplace=True)
# %%
# A function to plot arabic labels
def arabic_plot(labels: pd.Series):
    ArabicLabels = labels.apply(arabic_reshaper.reshape)
    result = []
    for label in ArabicLabels:
        result.append(get_display(label))
    if len(result) == 1:
        return result[0]
    else:
        return result

#%%
sns.set_theme()
sns.set_context("poster")
sns.barplot(y="price", x=arabic_plot(df["city"]), data=df)
plt.ylabel(arabic_plot(pd.Series("الأسعار ")))
plt.xlabel(arabic_plot(pd.Series("المدن")))
plt.title(arabic_plot(pd.Series(" أسعار الأجار حسب المدينة")))

#%%
df.columns = df.columns.str.strip()
#%%
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
#%% Check for unique values in city column
df['district'].unique()
len(df['district'].unique())
#%%
ny=df[df["city"] == "الرياض"]
ny
#%%
ny1=ny[ny['price'] > 400000]
#%%
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(ny1["district"]), data=ny1)
plt.ylabel(arabic_plot(pd.Series("الأسعار ")))
plt.xlabel(arabic_plot(pd.Series("أحياء مدينة الرياض")))
plt.title(arabic_plot(pd.Series(" أسعار الأجار حسب احياء مدينة الرياض")))

#%%
nj1=nj[nj['price'] > 40000]
#%%
nd1=nd[nd['price'] > 400000]

#%%
nk1=nk[nk['price'] > 100000]
nk1
#%%
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nj1["district"]), data=nj1)
plt.ylabel(arabic_plot(pd.Series("الأسعار ")))
plt.xlabel(arabic_plot(pd.Series("أحياء مدينة جدة")))
plt.title(arabic_plot(pd.Series(" أسعار الأجار حسب احياء مدينة جدة")))

#%%
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nd1["district"]), data=nd1)
plt.ylabel(arabic_plot(pd.Series("الأسعار ")))
plt.xlabel(arabic_plot(pd.Series("أحياء مدينة الدمام")))
plt.title(arabic_plot(pd.Series(" أسعار الأجار حسب احياء مدينة الدمام")))

#%%
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nk1["district"]), data=nk1)
plt.ylabel(arabic_plot(pd.Series("الأسعار ")))
plt.xlabel(arabic_plot(pd.Series("أحياء مدينة الخبر")))
plt.title(arabic_plot(pd.Series(" أسعار الأجار حسب احياء مدينة الخبر")))
#%%
df.groupby('city')["price"].mean()
#%%
df.groupby('city')["price"].min()
#%%
df.groupby('city')["price"].max()
#%%
df.groupby('city')["price"].median()
# Price per distract in each city??
#%%
sns.set_theme()
sns.set_context("poster")
sns.barplot(data=df,x="livingrooms",y="price")
plt.title(("livingrooms VS prices"))
plt.xlabel(("livingrooms"))
plt.ylabel(("Average prices"))
#%%
sns.set_theme()
sns.boxplot(data=df,x="bathrooms",y="price")
plt.title(("bathrooms VS prices"))
plt.xlabel(("bathrooms"))
plt.ylabel(("Average prices"))
# %%
locator = Nominatim(user_agent="myGeocoder")
geocode = RateLimiter(locator.geocode, min_delay_seconds=0.1)
df['location'] = df['district'].apply(geocode)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
#%%
df1 = pd.read_csv("../misk_skills/Assighnment/SA_Aqar_Added_Attributes.csv")
df1.drop('details', axis=1, inplace=True)
df1

# %%
# count the number of properties with some features in each city
sns.set_theme()
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, figsize=(15,10))
# `livingrooms > 2`
data_city = df[df["livingrooms"] > 2]
sns.histplot(ax=ax1, x=arabic_plot(data_city["city"]),color="red")
# `driver_room == 1`
data_driver_room = df[df["driver_room"] == 1]
sns.histplot(ax=ax2, x=arabic_plot(data_driver_room["city"]),color="red")
# `basement == 1`
data_basement = df[df["basement"] == 1]
sns.histplot(ax=ax3, x=arabic_plot(data_basement["city"]),color="red")
# `elevator == 1`
data_elevator = df[df["elevator"] == 1]
sns.histplot(ax=ax4, x=arabic_plot(data_elevator["city"]),color="red")
ax1.set_title("Number of properties with more than two Livingrooms")
ax2.set_title("Number of properties with Driver room")
ax3.set_title("Number of properties with Basement")
ax4.set_title("Number of properties with Elevator")
ax1.set_ylabel("Count")
ax2.set_ylabel("Count")
ax3.set_ylabel("Count")
ax4.set_ylabel("Count");

#%%
sns.set_theme()
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, figsize=(15,10))
# `fireplace`
data_city = df[df["fireplace"]  == 1]
sns.histplot(ax=ax1, x=arabic_plot(data_city["city"]),color="red")
# `garage`
data_driver_room = df[df["garage"] == 1]
sns.histplot(ax=ax2, x=arabic_plot(data_driver_room["city"]),color="red")
# `pool`
data_basement = df[df["pool"] == 1]
sns.histplot(ax=ax3, x=arabic_plot(data_basement["city"]),color="red")
# `bathrooms >3 `
data_elevator = df[df["bathrooms"] > 3]
sns.histplot(ax=ax4, x=arabic_plot(data_elevator["city"]),color="red")
ax1.set_title("Number of properties with fireplace")
ax2.set_title("Number of properties with garage")
ax3.set_title("Number of properties with pool")
ax4.set_title("Number of properties with more than three bathrooms")
ax1.set_ylabel("Count")
ax2.set_ylabel("Count")
ax3.set_ylabel("Count")
ax4.set_ylabel("Count");
# %%
import plotly.express as px
fig = px.imshow(df.corr())
fig
#%%
corr = df.corr()
kot = corr[corr>=.5]
plt.figure(figsize=(12,8))
sns.heatmap(kot, cmap="Greens")
#%%
# driver_room`
sns.set_theme()
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, figsize=(15,10))
ax1 = sns.barplot(ax=ax1, y=df["price"], x=df["driver_room"] ,data=df)
ax1.set_xlabel("")
labels = [item.get_text() for item in ax1.get_xticklabels()]
labels[0] = "Without Driver Room"
labels[1] = "With Driver Room"
ax1.set_xticklabels(labels)
ax1.set_ylabel("Price")

# ac
ax2 = sns.barplot(ax=ax2, y=df["price"], x=df["ac"] ,data=df)
ax2.set_xlabel("")
labels = [item.get_text() for item in ax2.get_xticklabels()]
labels[0] = "Without AC"
labels[1] = "With AC"
ax2.set_xticklabels(labels)
ax2.set_ylabel("Price")

# pool
ax3 = sns.barplot(ax=ax3, y=df["price"], x=df["pool"] ,data=df)
ax3.set_xlabel("")
labels = [item.get_text() for item in ax3.get_xticklabels()]
labels[0] = "Without Pool"
labels[1] = "With Pool"
ax3.set_xticklabels(labels)
ax3.set_ylabel("Price")

# basement
ax4 = sns.barplot(ax=ax4,y=df["price"], x=df["basement"] ,data=df)
ax4.set_xlabel("")
labels = [item.get_text() for item in ax4.get_xticklabels()]
labels[0] = "Without Basement"
labels[1] = "With Basement"
ax4.set_xticklabels(labels)
ax4.set_ylabel("Price");

#%%
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(df["front"]), data=df)
# front per city??
#%%
#df.columns
df['front'].unique()
#%%
ny=df[df["city"] == "الرياض"]
ny
#%%
nj=ny=df[df["city"] == "جدة"]
nj
#%%
nd=ny=df[df["city"] == "الدمام"]
nd
#%%
nk=ny=df[df["city"] == "الخبر"]
nk
#%%
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(ny["front"]), data=ny)

#%%
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nj["front"]), data=nj)
#%%
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nd["front"]), data=nd)

#%%
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nk["front"]), data=nk)

# Which city has the highest/lowest rent rate?
# Does the district within a city correlate with the rent rate?
# Do the number of features within a house increase its rent rate?
