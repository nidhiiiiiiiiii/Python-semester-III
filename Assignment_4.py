def fibonacci_memo(n, memo):
    # Base cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    # If already calculated, return the stored value
    if memo[n] != -1:
        return memo[n]

    # Calculate and store the result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


# Take input from the user
n = int(input("Enter n: "))

# Create a list to store results
memo = [-1] * (n + 1)

# Find Fibonacci number
answer = fibonacci_memo(n, memo)

print("Fibonacci number:", answer)

def fibonacci_tabulation(n):

    # Base cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    # Create a table
    dp = [0] * (n + 1)

    # First two Fibonacci numbers
    dp[0] = 0
    dp[1] = 1

    # Calculate remaining values
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Take input from the user
n = int(input("Enter n: "))

# Find Fibonacci number
answer = fibonacci_tabulation(n)

print("Fibonacci number:", answer)
