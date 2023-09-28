# This module contains functions that are useful for data epxloration on any dataset stored in a DataFrame
import pandas as pd
from pathlib import Path

def dataset_info(df):
# Create a DataFrame to contain all the information about the dataset
    # Get the columns from the dataset
    columns = df.columns.to_list()

    # Add the columns to a dictionary
    info_dict = {'columns': columns}

    # Transform the dictionary into a DataFrame
    info_df = pd.DataFrame(info_dict)

    # Add columns to store the info
    info_df['dtypes'] = ''
    info_df['elements'] = 0
    info_df['missing'] = 0
    info_df['unique'] = 0

    # Initialise counter
    count = 0

    # Get information for all columns
    for col in columns:
        info_df.iloc[count,1] = str(df[col].dtypes)
        info_df.iloc[count,2] = df[col].count()
        info_df.iloc[count,3] = len(df) - df[col].count()
        info_df.iloc[count,4] = df[col].nunique()
        count += 1

    return info_df
