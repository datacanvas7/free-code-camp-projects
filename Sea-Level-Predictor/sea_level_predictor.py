import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.6, label='Data Points')

    # First line of best fit (all data)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = np.arange(df['Year'].min(), 2051)
    y_pred1 = res1.intercept + res1.slope * x_pred1
    plt.plot(x_pred1, y_pred1, 'r', label='Best Fit Line (1880-2013)')

    # Second line of best fit (from year 2000)
    recent_df = df[df['Year'] >= 2000]
    res2 = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    x_pred2 = np.arange(2000, 2051)
    y_pred2 = res2.intercept + res2.slope * x_pred2
    plt.plot(x_pred2, y_pred2, 'green', linestyle='--', label='Best Fit Line (2000-2013)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()