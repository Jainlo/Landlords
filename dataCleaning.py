import pandas as pd
import numpy as np
import arabic_reshaper


#%% Reading the data
def clean():
    df = pd.read_csv('SA_Aqar.csv')
    # 1. Do we have missing data? yes
    # In details column - 80 NAs
    df.isnull().sum()

    # 2. Details column has missing data and is made up of unstructured data
    # We can drop it 
    df.drop('details', axis=1, inplace=True)

    # 3. Do we have any duplicates?
    # First clean whitespace to be able to compare values
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    # Clean column names as well
    df.columns = df.columns.str.strip()
    # Check for duplicates 
    df[~df.duplicated()]# Check source and where did the duplication come from
    # Remove duplicates
    df = df[~df.duplicated()]
