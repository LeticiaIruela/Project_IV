import pandas as pd
import re

def unique_values (df):
    unique_values = {}
    for column in df.columns:
        unique_values[column] = df[column].unique()
    for column, unique_values in unique_values.items():
        print(f"{column}:")
        print(unique_values)
        print()

def verifystring (df, column_name):
    unique_values = df[column_name].unique()
    allstring = all(isinstance(x, str) for x in unique_values)
    if allstring:
        print("All values are strings")
    else:
        print("Not only strings in the column")

def cleaning(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df = df.drop('Row ID', axis=1)
    return df

def round_numerical (df, columns):
    df[columns]=df[columns].round(2)
    return df

def convert_to_datetime(df, columns):
    df[columns] = pd.to_datetime(df[columns], format='%m/%d/%Y')
    return df
