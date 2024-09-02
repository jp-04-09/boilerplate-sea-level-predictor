import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df.info())

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    resA = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    # Create a range of years from the minimum year to 2050
    years_range_A = np.arange(min(df["Year"]), 2051)
    plt.plot(years_range_A, resA.intercept + resA.slope*years_range_A)

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    resB = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    years_range_B = np.arange(2000, 2051)
    plt.plot(years_range_B, resB.intercept + resB.slope*years_range_B)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()