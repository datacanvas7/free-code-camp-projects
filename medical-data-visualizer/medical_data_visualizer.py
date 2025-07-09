import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
def load_data():
    df = pd.read_csv('medical_examination.csv')
    return df

# Add 'overweight' column
def calculate_overweight(df):
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)  # Fixed parentheses
    return df

# Normalize data
def normalize_data(df):
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
    return df

# Draw categorical plot
def draw_cat_plot():
    df = load_data()
    df = calculate_overweight(df)
    df = normalize_data(df)

# Create DataFrame for cat plot
    df_cat = pd.melt(df, id_vars=['cardio'], 
                         value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

# Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat = df_cat.rename(columns={'size': 'total'})

# Draw the catplot
    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', 
                    data=df_cat, kind='bar')
    fig = g.fig

    return fig

# Draw heat map
def draw_heat_map():
    df = load_data()

# Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &  # Fixed line continuation
        (df['height'] <= df['height'].quantile(0.975)) &  # Fixed line continuation
        (df['weight'] >= df['weight'].quantile(0.025)) &  # Fixed line continuation
        (df['weight'] <= df['weight'].quantile(0.975))]  # Fixed parentheses

# Calculate the correlation matrix
    corr = df_heat.corr()

# Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

# Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', 
                center=0, vmin=-0.5, vmax=0.5, 
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    return fig