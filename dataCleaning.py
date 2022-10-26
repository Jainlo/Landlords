import pandas as pd
import numpy as np
import arabic_reshaper


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
