import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def heatmap_profitability(df):
    df_grouped = df.groupby(['Segments', 'Category'])['Profit'].sum().reset_index()
    pivot_table = df_grouped.pivot(index='Segments', columns='Category', values='Profit')
    normalized_pivot = (pivot_table - pivot_table.min().min()) / (pivot_table.max().max() - pivot_table.min().min())
    plt.figure(figsize=(10, 6))
    sns.heatmap(normalized_pivot, annot=True, cmap='YlGnBu', vmin=0, vmax=1)
    plt.title('Profitability per segment and Category')
    plt.xlabel('Category')
    plt.ylabel('Segment')
    plt.savefig('fig/heatmap_profitability.png')
    plt.show()