import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, encoding='latin-1')
    return df

def to_csv(df, file_path):
    df.to_csv(file_path, index=False)

def to_xlsx(df, file_path):
    df.to_excel(file_path, index=False)
