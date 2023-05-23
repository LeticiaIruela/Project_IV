from sklearn.linear_model import LinearRegression
import pandas as pd

def linear_regression_analysis(df):
    regression_model = LinearRegression()
    X = df[['Sales', 'Discount']]
    y = df['Profit']
    regression_model.fit(X, y)
    coefficients = regression_model.coef_
    intercept = regression_model.intercept_
    print("Coefficients:", coefficients)
    print("Intercept:", intercept)

def profit_discount_corr(df):
    filtered_data = df[(df['Segments'].isin(['New Customers', 'Potential Loyalist', 'Promising'])) &
                            (df['Order Date'].dt.year == 2017)]
    result = filtered_data.groupby(['Segments', filtered_data['Order Date'].dt.year, 'Category']).agg({
        'Profit': 'sum',
        'Sales': 'sum'
    }).reset_index()
    result = result.sort_values(by='Sales', ascending=False)
    return result

