# 1. TOP-DOWN APPROACH (Memoization / Recursion + Cache)
def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    # Create a memoization table initialized with -1
    # Rows represent items, columns represent remaining capacity
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n)]

    def solve(index, current_capacity):
        # Base case: No items left or no capacity left
        if index == n or current_capacity == 0:
            return 0

        # Check if the result is already calculated
        if memo[index][current_capacity] != -1:
            return memo[index][current_capacity]

        # Option 1: Skip the current item
        exclude_item = solve(index + 1, current_capacity)

        # Option 2: Take the current item (only if it fits)
        include_item = 0
        if weights[index] <= current_capacity:
            include_item = values[index] + solve(
                index + 1, current_capacity - weights[index]
            )

        # Store the maximum of both options in the memo table
        memo[index][current_capacity] = max(exclude_item, include_item)
        return memo[index][current_capacity]

    return solve(0, capacity)


# 2. BOTTOM-UP APPROACH (Tabulation / Iterative Table Building)
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    # Create a 2D table grid (n + 1 rows by capacity + 1 columns) initialized with 0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table grid iteratively from the ground up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Check if the weight of the current item is less than the current capacity
            if weights[i - 1] <= w:
                # Max of: including the item OR excluding the item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )
            else:
                # If it doesn't fit, carry over the value from the previous item row
                dp[i][w] = dp[i - 1][w]

    # The bottom-right cell contains the maximum value possible
    return dp[n][capacity]


# --- Driver Code to Test the Functions ---
if __name__ == "__main__":
    # Sample Problem Data
    item_values = [60, 100, 120]
    item_weights = [10, 20, 30]
    max_capacity = 50

    print(f"Items Weights: {item_weights}")
    print(f"Items Values:  {item_values}")
    print(f"Max Capacity:  {max_capacity}\n")

    # Run Top-Down
    max_val_td = knapsack_top_down(item_weights, item_values, max_capacity)
    print(f"Maximum Value (Top-Down Approach): {max_val_td}")

    # Run Bottom-Up
    max_val_bu = knapsack_bottom_up(item_weights, item_values, max_capacity)
    print(f"Maximum Value (Bottom-Up Approach): {max_val_bu}")
