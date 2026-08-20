# Program to find Longest Common Subsequence (LCS)
# Using Dynamic Programming - Bottom-Up approach


# Take two sequences from the user
seq1 = input("Enter first sequence: ")
seq2 = input("Enter second sequence: ")

# Find the lengths of both sequences
m = len(seq1)
n = len(seq2)

# Create a DP table
# The table has (m+1) rows and (n+1) columns
dp = [[0 for j in range(n + 1)] for i in range(m + 1)]


# Fill the DP table
for i in range(1, m + 1):

    for j in range(1, n + 1):

        # If characters are the same
        if seq1[i - 1] == seq2[j - 1]:

            dp[i][j] = dp[i - 1][j - 1] + 1

        # If characters are different
        else:

            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


# The last cell contains the length of LCS
print("Length of LCS =", dp[m][n])


# Find the actual LCS
i = m
j = n

lcs = ""

while i > 0 and j > 0:

    # If characters are the same
    if seq1[i - 1] == seq2[j - 1]:

        lcs = seq1[i - 1] + lcs

        i = i - 1
        j = j - 1

    # Move to the larger value
    elif dp[i - 1][j] > dp[i][j - 1]:

        i = i - 1

    else:

        j = j - 1


print("Longest Common Subsequence =", lcs)