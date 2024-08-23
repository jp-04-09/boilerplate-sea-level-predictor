import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df.info())

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.plot(df["Year"], res.intercept + res.slope*df["Year"], 'r', label='fitted line')

    # Create second line of best fit


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()