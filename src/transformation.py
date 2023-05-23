import pandas as pd
import re
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def extract_date_parts(df,columns):
    for column in columns:
        df[column + '_Year'] = pd.to_datetime(df[column], format='%m/%d/%Y').dt.year
        df[column + '_Month'] = pd.to_datetime(df[column], format='%m/%d/%Y').dt.month
        df[column + '_Day'] = pd.to_datetime(df[column], format='%m/%d/%Y').dt.day
    return df

def calc_rfm(df):
    recency = df.groupby('Customer ID')['Order Date'].max()
    recency = pd.to_datetime('2018-01-30') - recency
    frequency = df.groupby('Customer ID').size()
    monetary = df.groupby('Customer ID')['Sales'].sum()
    df_summary = pd.DataFrame({'Recency': recency, 'Frequency': frequency, 'Monetary': monetary}).reset_index()
    df = df.merge(df_summary, on='Customer ID', how='left')
    return df

def normalization_rfm(df):
    recency = df['Recency'].dt.days 
    frequency = df['Frequency']
    monetary = df['Monetary']
    scaler = MinMaxScaler()
    recency_norm = scaler.fit_transform(np.array(recency).reshape(-1, 1))
    frequency_norm = scaler.fit_transform(np.array(frequency).reshape(-1, 1))
    monetary_norm = scaler.fit_transform(np.array(monetary).reshape(-1, 1))
    recency_norm = np.round(recency_norm, 2)
    frequency_norm = np.round(frequency_norm, 2)
    monetary_norm = np.round(monetary_norm, 2)
    df['Recency_Normalized'] = recency_norm
    df['Frequency_Normalized'] = frequency_norm
    df['Monetary_Normalized'] = monetary_norm
    return df

def scoring_rfm(df):
    df['RecencyScore'] = np.where(df['Recency_Normalized'] <= 0.2, 5,
                                   np.where(df['Recency_Normalized'] <= 0.4, 4,
                                            np.where(df['Recency_Normalized'] <= 0.6, 3,
                                                     np.where(df['Recency_Normalized'] <= 0.8, 2, 1))))

    df['FrequencyScore'] = np.where(df['Frequency_Normalized'] <= 0.2, 1,
                                     np.where(df['Frequency_Normalized'] <= 0.4, 2,
                                              np.where(df['Frequency_Normalized'] <= 0.6, 3,
                                                       np.where(df['Frequency_Normalized'] <= 0.8, 4, 5))))

    df['MonetaryScore'] = np.where(df['Monetary_Normalized'] <= 0.2, 1,
                                    np.where(df['Monetary_Normalized'] <= 0.4, 2,
                                             np.where(df['Monetary_Normalized'] <= 0.6, 3,
                                                      np.where(df['Monetary_Normalized'] <= 0.8, 4, 5))))
    return df

def total_RFM(df):
    df['RFM Score'] = df['RecencyScore'].astype(str) + df['FrequencyScore'].astype(str) + df['MonetaryScore'].astype(str)
    return df

def customer_segmentation(df):
    df['Segments'] = 'Other'
    df.loc[df['RFM Score'].isin(['555', '554', '544', '545', '454', '455', '445']), 'Segments'] = 'Champions'
    df.loc[df['RFM Score'].isin(['543', '444', '435', '355', '354', '345', '344', '335']), 'Segments'] = 'Loyal customer'
    df.loc[df['RFM Score'].isin(['553', '551', '552', '541', '542', '533', '532', '531', '452', '451', '442', '441', '431', '453', '433', '432', '423', '353', '352', '351', '342', '341', '333', '323']), 'Segments'] = 'Potential Loyalist'
    df.loc[df['RFM Score'].isin(['512', '511', '422', '421', '412', '411', '311']), 'Segments'] = 'New Customers'
    df.loc[df['RFM Score'].isin(['525', '524', '523', '522', '521', '515', '514', '513', '425', '424', '413', '414', '415', '315', '314', '313']), 'Segments'] = 'Promising'
    df.loc[df['RFM Score'].isin(['535', '534', '443', '434', '343', '334', '325', '324']), 'Segments'] = 'Need Attention'
    df.loc[df['RFM Score'].isin(['155', '154', '144', '214', '215', '115', '114', '113']), 'Segments'] = 'Cannot Lose Them'
    df.loc[df['RFM Score'].isin(['331', '321', '312', '221', '213']), 'Segments'] = 'About to sleep'
    df.loc[df['RFM Score'].isin(['255', '254', '245', '244', '253', '252', '243', '242', '235', '234', '225', '224', '153', '152', '145', '143', '142', '135', '134', '133', '125', '124']), 'Segment'] = 'At risk'
    df.loc[df['RFM Score'].isin(['332', '322', '231', '241', '251', '233', '232', '223', '222', '132', '123', '122', '212', '211']), 'Segments'] = 'Hibernating'
    df.loc[df['RFM Score'].isin(['111', '112', '121', '131', '141', '151']), 'Segments'] = 'Lost'
    return df