import pandas as pd
import numpy as np
# import arabic_reshaper


# Reading the data
def clean(df: pd.DataFrame) -> pd.DataFrame:
    print(df.info())
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

    return df