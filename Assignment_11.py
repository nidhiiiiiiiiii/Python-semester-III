import numpy as np
import pandas as pd

# Set a random seed for reproducible results
np.random.seed(42)

# 1. Create a Pandas Series containing 10 random numbers
data = pd.Series(np.random.randint(1, 100, size=10), name="Random_Numbers")

print("--- Initial Series ---")
print(data)

# 2. Indexing Operations
first_element = data[0]  # Access by index position
subset = data[2:6]  # Slice from index 2 to 5

print("\n--- Indexing ---")
print(f"First element: {first_element}")
print("Slice (indices 2 to 5):")
print(subset)

# 3. Filtering Operations
greater_than_50 = data[data > 50]  # Boolean indexing

print("\n--- Filtering (Values > 50) ---")
print(greater_than_50)

# 4. Statistical Operations
mean_val = data.mean()
median_val = data.median()
min_val = data.min()
max_val = data.max()
std_val = data.std()

print("\n--- Statistical Operations ---")
print(f"Mean:   {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Min:    {min_val}")
print(f"Max:    {max_val}")
print(f"Std:    {std_val:.2f}")