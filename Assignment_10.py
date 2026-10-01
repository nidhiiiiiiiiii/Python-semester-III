import numpy as np

# 1. Create a 1D array with numbers from 1 to 10
# np.arange(start, stop) goes up to, but does not include, the stop number
numbers = np.arange(1, 11)
print("Our Array:")
print(numbers)
print("-" * 30)

# 2. Slicing (Extracting a part of the array)
# Remember: Python counting starts at 0!
# [2:7] gets elements from index 2 up to index 6
middle_part = numbers[2:7]
print("Sliced Array (index 2 to 6):")
print(middle_part)
print("-" * 30)

# 3. Basic Math & Statistics
# NumPy has built-in tools to look at your data instantly
print("Statistical Measures:")
print("Total Sum:", np.sum(numbers))
print("Average (Mean):", np.mean(numbers))
print("Highest Number (Max):", np.max(numbers))
print("Lowest Number (Min):", np.min(numbers))
print("-" * 30)

# 4. Broadcasting (Modifying every number at once)
# Instead of using a loop, you can multiply or add to the whole array directly
doubled_numbers = numbers * 2
print("Broadcasting Result (Every number multiplied by 2):")
print(doubled_numbers)
