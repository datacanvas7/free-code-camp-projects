import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator
import numpy as np

# Import data
def import_data():
    """Import and preprocess the forum page views data"""
    df = pd.read_csv('fcc-forum-pageviews.csv', 
                    parse_dates=['date'], 
                    index_col='date')
    return df

# Clean data
def clean_data(df):
    """Remove outliers (top and bottom 2.5% of page views)"""
    val = df['value']
    df_clean = df[
        (val >= val.quantile(0.025)) & 
        (val <= val.quantile(0.975))
    ]
    return df_clean

# Draw line plot
def draw_line_plot():
    """Create and save a line plot of daily page views"""
    df = clean_data(import_data())

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='firebrick', linewidth=1)

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig

# Draw bar plot
def draw_bar_plot():
    """Create and save a bar plot of average monthly views by year"""
    df = clean_data(import_data())

    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Calculate monthly averages
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Order months chronologically
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[months]

    # Plot
    fig = df_bar.plot(kind='bar', figsize=(10, 7), 
                     xlabel='Years', ylabel='Average Page Views').figure
    plt.legend(title='Months')
    plt.tight_layout()

    fig.savefig('bar_plot.png')
    return fig

# Draw box plots
def draw_box_plot():
    """Create and save box plots of yearly and monthly distributions"""
    df = clean_data(import_data())

    # Prepare DataFrame
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]

    # Set up figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

    # Yearly boxplot
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # Monthly boxplot
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Adjust layout and save
    plt.tight_layout()
    fig.savefig('box_plot.png')
    return fig