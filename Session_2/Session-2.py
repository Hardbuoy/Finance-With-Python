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
           


