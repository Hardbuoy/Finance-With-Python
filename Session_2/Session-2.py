# Essential Data Science Libraries: pandas, numpy and matplotlib
import pandas  # importing just to show version number
import numpy  # importing just to show version number
import matplotlib # importing just to show version number

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#create a simple dataframe with pandas
data = {
    "Stocks": ["AAPL", "JPH", "MSFI"],
    "Prices": [150.75, 100.50, 200],
    "Shares": [10, 15, 25]
}


df = pd.DataFrame(data)
print(f"Data Dictionary: {data}\n")
print("\nSimple DataFrame:\n")

print(df)

# use numpy for numerical operations
prices = np.array([150.75, 100.50, 200])
Average_price = np.mean(prices)
print(f"Average Stock Price: ${Average_price:.2f}")

price_sum = np.sum(prices)
print(f"Sum of Stock Prices: ${price_sum:.2f}")

price_min = np.min(prices)
print(f"Min Stock Prices: ${price_min:.2f}")

price_max = np.max(prices)
print(f"Max Stock Prices: ${price_max:.2f}")

price_median = np.median(prices)
print(f"Median of Stock Prices: ${price_median:.2f}")

price_std = np.std(prices)
print(f"Standard Deviation of Stock Prices: ${price_std:.2f}")


# plot with matplotlib
plt.figure(figsize=(8, 4))
plt.plot(prices, marker="o", linestyle=":", color="green")
plt.title("Stock Prices Over Time")
plt.xlabel("time (arbitrary units)")
plt.ylabel("price")
plt.grid(True)
plt.show()

# Mini "Hello Finace" Project: Simulate and Plot a Random Walk

#Random Walk: Simple model for Simulating Stock Price movement
#Assumption is that price changes are random and unpredictable.
#Read more about Random Walks

# use seed - This ensures reproducibility, same random numbers each run
np.random.seed(42) # if you want truely random numbers each run, remove this line
Random_walk_no_cumulative_sum = np.random.normal(0, 1, 250)
print(f"first 20 values of Random_walk no cumulative sum\n {Random_walk_no_cumulative_sum[0:20]}")

Random_walk = np.random.normal(0, 1, 250).cumsum()
print(f"first 20 values of Random_walk\n {Random_walk[0:20]}")


mean_walk_no_sum =  np.mean(Random_walk_no_cumulative_sum)
std_walk_no_sum =  np.std(Random_walk_no_cumulative_sum)

print(f"Mean of no sum: {mean_walk_no_sum}")
print(f"Standard Deviation of no sum: {std_walk_no_sum}")



mean_walk =  np.mean(Random_walk)
std_walk =  np.std(Random_walk)

print(f"Mean: {mean_walk}")
print(f"Standard Deviation: {std_walk}")

plt.figure(figsize=(20, 8))

plt.plot(Random_walk, marker=".", linestyle="-", color="green")
plt.title("Simulated Random Walk(Stock Price Simulation)")
plt.xlabel("Time(Days)")
plt.ylabel("Simulated Stock Price")
plt.grid(True)
plt.show()

plt.figure(figsize=(20, 8))
plt.plot(Random_walk_no_cumulative_sum, marker=".", linestyle="-", color="green")
plt.title("Simulated Random Walk(No Cumulative Sum)")
plt.xlabel("Time(Days)")
plt.ylabel("Simulated Stock Price")
plt.grid(True)
plt.show()


# plot Normal Distribution vrs Cumulative sum of normal Distribution
plt.figure(figsize=(20, 8))
plt.plot(
    Random_walk_no_cumulative_sum,
    marker=".",
    linestyle="-",
    color="orange",
    label="Random Walk No CumSum"
)

plt.plot(
   Random_walk,
    marker=".",
    linestyle="-",
    color="purple",
    label="Random Walk with Cumulative Sum"
)

plt.title("Random Walk No CumSum vrs Random Walk with Cumulative Sum")
plt.xlabel("Time(days)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()


# Reading Real Financial Data from CSV files
# Read stock price data of AAPL, MSFT, JPM from csv files.
# Perform some analysis on the data.
# Merge the data and plot them using matplotlib and plotly.

# Read CSV files using pandas

aapl = pd.read_csv("AAPL.CSV")
jpm = pd.read_csv("JPM.CSV")
msft = pd.read_csv("MSFT.CSV")

# Display top 5 and last 5 using head and tail


print(f"\nAAPL DATA: {aapl.head()}\n")
print(aapl.tail())

print(f"\nMSFT DATA: {msft.head()}\n")
print(msft.tail())

print(f"\nJPM DATA: {jpm.head()}\n")
print(jpm.tail())

# Dispaly a summary of AAPL's Data
print("\nSummary of Data:")

print(aapl.describe())


# Display summary and other details of MSFT's Data
print(msft.describe())

print(f"Shape: {msft.shape}")
print(f"Columns: {msft.columns}")
print(f"Number of Rows: {len(msft)}")
print(f"Data Types: {msft.dtypes}")
print(f"Date Range: {msft['Date'].min()} to {msft['Date'].max()}")
print(f"\nUnique Values in HIgh: {msft['High'].unique()}\n")
print(f"\nValue Count: {msft['Low'].value_counts()}\n")

# merge the closing prices of each stock base on the 'Date' column
merged_data = pd.merge(
    aapl[["Date", "Close"]],
    msft[["Date", "Close"]],
    on="Date",
    suffixes=("_AAPL", "_MSFT") 
)

merged_data = pd.merge(
    merged_data,
    jpm[["Date", "Close"]],
    on="Date",
)

merged_data.rename(columns={"Close": "Close_JPM"}, inplace=True) # inplace=True modifies original Dataframe
print(merged_data.head(10)) #top 10 rows

# plot the closing prices of AAPL, JPM and MSFT
plt.figure(figsize=(20, 15))

plt.plot(merged_data["Date"], merged_data["Close_AAPL"], label="AAPL", marker="o")
plt.plot(merged_data["Date"], merged_data["Close_MSFT"], label="MSFT", marker="o") 
plt.plot(merged_data["Date"], merged_data["Close_JPM"], label="JPM", marker="o")
plt.title("Stock Prices of AAPL, MSFT AND JPM")
plt.ylabel("Close Prices")
plt.xlabel("Date")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


import plotly.graph_objects as go
import plotly
print(f"Version of plotly: {plotly.__version__}")

# plot the closing prices of AAPL, JPM and MSFT using plotly
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=merged_data["Date"],
        y=merged_data["Close_AAPL"],
        mode="lines+markers",
        name="AAPL"
    )
)

fig.add_trace(
    go.Scatter(
        x=merged_data["Date"],
        y=merged_data["Close_MSFT"],
        mode="lines+markers",
        name="MSFT"
    )
)

fig.add_trace(
    go.Scatter(
        x=merged_data["Date"],
        y=merged_data["Close_JPM"],
        mode="lines+markers",
        name="JPM"
    )
)

fig.update_layout(
    title="Closing prices Comparison: AAPL, JPM AND MSFT",
    xaxis_title="Date",
    yaxis_title="Closing Prices",
     xaxis_tickangle=45
    
    
)

fig.show()
           


