# Best time to buy and sell stock #
# Intuition : If you are selling at the i-th day make sure you choose
#             The day for 0 to i-1 when the stock was at minimum price

def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    mini = prices[0]
    profit = 0 # Initial condition
    for i in prices:
        cost = i - mini  # To find the profit
        profit = max(cost, profit) # To find the current maximum profit
        mini = min(i, mini) # to find the current minimum price from 0th day to ith day
    return profit
