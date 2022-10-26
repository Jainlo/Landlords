

#%%
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display

#%%
# Upload and clean the data
df = pd.read_csv("../misk_skills/Assighnment/SA_Aqar.csv")
#%% Reading the data
def clean(df: pd.DataFrame):

# 2. Details column has missing data and is made up of unstructured data
# We can drop it
 df.drop('details', axis=1, inplace=True)

# 3. Do we have any duplicates?
# First clean whitespace to be able to compare values
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
# Clean column names as well
df.columns = df.columns.str.strip()

# Remove duplicates
df = df[~df.duplicated()]

#%% Remove the rows that have the same value in price and size
df = df[df['price'] != df['size']]

#%% Remove fronts that are equal to '3 شوارع'
df = df[df['front'] != '3 شوارع']

#%% Remove fronts that are equal to '4 شوارع'
df = df[df['front'] != '4 شوارع']

#%% Remove values with a size < 100
df = df[df['size'] > 100]
#%%
# remove the spaces in the columns names
df.columns = df.columns.str.strip()
#%%
# remove the spaces in the columns values
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)   
#%%
clean(df)
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
# rental price per city
sns.set_theme()
sns.barplot(y="price", x=arabic_plot(df["city"]), data=df,color = '0.4',ci=None)
plt.ylabel("Price")
plt.title("Rental price for each city")
#%%
# Extract specific city
ny=df[df["city"] == "الرياض"]
#%%
nj=df[df["city"] == "جدة"]
#%%
nd=df[df["city"] == "الدمام"]
#%%
nk=df[df["city"] == "الخبر"]
#%%
ny1=ny[ny['price'] > 550000]
#%%
# Price per distract in each city?? Only the top
sns.set_theme()
plt.subplots(figsize=(12,7))
sns.barplot(y="price", x=arabic_plot(ny1["district"]), data=ny1,color = '0.4',ci=None)
plt.ylabel(arabic_plot(pd.Series("price")))
plt.title("Rental price for Riyadh district ")
#%%
nj1=nj[nj['price'] > 350000]
#%%
nd1=nd[nd['price'] > 135000]
#%%
nk1=nk[nk['price'] > 150000]
#%%
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nj1["district"]), data=nj1,color = '0.4',ci=None)
plt.ylabel(arabic_plot(pd.Series("price")))
plt.title("Rental price for Jeddah district ")

#%%
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nd1["district"]), data=nd1,color = '0.4',ci=None)
plt.ylabel(arabic_plot(pd.Series("price")))
plt.title("Rental price for Dammam district ")

#%%
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nk1["district"]), data=nk1,color = '0.4',ci=None)
plt.ylabel(arabic_plot(pd.Series("price")))
plt.title("Rental price for Khobar district ")
#%%
##  Check livingrooms vs price
sns.set_theme()
#sns.set_context("poster")
sns.barplot(data=df,x="livingrooms",y="price",color = '0.4',ci=None)
plt.title(("livingrooms VS prices"))
plt.xlabel(("livingrooms"))
plt.ylabel(("Average prices"))
#%%
#Check livingrooms vs price
sns.set_theme()
sns.barplot(data=df,x="bathrooms",y="price",color = '0.4',ci=None)
plt.title(("bathrooms VS prices"))
plt.xlabel(("bathrooms"))
plt.ylabel(("Average prices"))
# %%
# count the number of properties with some features in each city
sns.set_theme()
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, figsize=(15,10))
# `livingrooms > 2`
data_city = df[df["livingrooms"] > 2]
sns.histplot(ax=ax1, x=arabic_plot(data_city["city"]),color = '0.4')
# `driver_room == 1`
data_driver_room = df[df["driver_room"] == 1]
sns.histplot(ax=ax2, x=arabic_plot(data_driver_room["city"]),color = '0.4')
# `basement == 1`
data_basement = df[df["basement"] == 1]
sns.histplot(ax=ax3, x=arabic_plot(data_basement["city"]),color = '0.4')
# `elevator == 1`
data_elevator = df[df["elevator"] == 1]
sns.histplot(ax=ax4, x=arabic_plot(data_elevator["city"]),color = '0.4')
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
sns.histplot(ax=ax1, x=arabic_plot(data_city["city"]),color = '0.4')
# `garage`
data_driver_room = df[df["garage"] == 1]
sns.histplot(ax=ax2, x=arabic_plot(data_driver_room["city"]),color = '0.4')
# `pool`
data_basement = df[df["pool"] == 1]
sns.histplot(ax=ax3, x=arabic_plot(data_basement["city"]),color = '0.4')
# `bathrooms >3 `
data_elevator = df[df["bathrooms"] > 3]
sns.histplot(ax=ax4, x=arabic_plot(data_elevator["city"]),color = '0.4')
ax1.set_title("Number of properties with fireplace")
ax2.set_title("Number of properties with garage")
ax3.set_title("Number of properties with pool")
ax4.set_title("Number of properties with more than three bathrooms")
ax1.set_ylabel("Count")
ax2.set_ylabel("Count")
ax3.set_ylabel("Count")
ax4.set_ylabel("Count");
#%%
# Investigating prices with and without some features 
# driver_room`
sns.set_theme()
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, figsize=(15,10))
ax1 = sns.barplot(ax=ax1, y=df["price"], x=df["driver_room"] ,data=df,ci=None)
ax1.set_xlabel("")
labels = [item.get_text() for item in ax1.get_xticklabels()]
labels[0] = "Without Driver Room"
labels[1] = "With Driver Room"
ax1.set_xticklabels(labels)
ax1.set_ylabel("Price")

# ac
ax2 = sns.barplot(ax=ax2, y=df["price"], x=df["ac"] ,data=df,ci=None)
ax2.set_xlabel("")
labels = [item.get_text() for item in ax2.get_xticklabels()]
labels[0] = "Without AC"
labels[1] = "With AC"
ax2.set_xticklabels(labels)
ax2.set_ylabel("Price")

# pool
ax3 = sns.barplot(ax=ax3, y=df["price"], x=df["pool"] ,data=df,ci=None)
ax3.set_xlabel("")
labels = [item.get_text() for item in ax3.get_xticklabels()]
labels[0] = "Without Pool"
labels[1] = "With Pool"
ax3.set_xticklabels(labels)
ax3.set_ylabel("Price")

# basement
ax4 = sns.barplot(ax=ax4,y=df["price"], x=df["basement"] ,data=df,ci=None)
ax4.set_xlabel("")
labels = [item.get_text() for item in ax4.get_xticklabels()]
labels[0] = "Without Basement"
labels[1] = "With Basement"
ax4.set_xticklabels(labels)
ax4.set_ylabel("Price");

#%%
# check which front is the most expensive in each city
sns.set_theme()
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(ny["front"]), data=ny,color = '0.4',ci=None)
plt.title(("Rental prices based on front in Riyadh"))
#%%
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nj["front"]), data=nj,color = '0.4',ci=None)
plt.title(("Rental prices based on front in Jeddah"))
#%%
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nd["front"]), data=nd,color = '0.4',ci=None)
plt.title(("Rental prices based on front in Dammam"))
#%%
plt.subplots(figsize=(10,7))
sns.barplot(y="price", x=arabic_plot(nk["front"]), data=nk,color = '0.4',ci=None)
plt.title(("Rental prices based on front in Khobar"))

