def knapsack_max_profit(weights, values, capacity):
    num_items = len(weights)
    # Create a table to store the maximum profit for each capacity and item
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]
    
    for i in range(1, num_items + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                # If the current item can be included, calculate the maximum of including and excluding it
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                # If the current item cannot be included, take the value from the previous row
                dp[i][j] = dp[i - 1][j]
    
    return dp[num_items][capacity]

# Example usage
weights = [2, 3, 4, 5]  # Weights of the coffee beans in pounds
values = [10, 20, 30, 40]  # Values (cost in rupees) of the coffee beans
capacity = 10  # Capacity of the bag in pounds
max_profit = knapsack_max_profit(weights, values, capacity)
print("Maximum Profit:", max_profit)
