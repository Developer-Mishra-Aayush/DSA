"""
Title: Coin Change (Recursive)
Approach: Try each coin that does not exceed remaining amount; recursively solve for amount - coin and take the minimum number of coins; base case amount == 0 returns 0, unreachable states return infinity
Time: Exponential without memoization (branches by coin choices)
Space: O(amount) - recursion depth in worst case
"""

def solve(coins,amount):
    if amount == 0:
        return 0
    minCoins = float('inf')

    for i in coins:
        if amount>=i:
            ans = solve(coins,amount-i)
            if ans!=float('inf'):
                coinused = 1+ans
                minCoins = min(coinused,minCoins)
    return minCoins

def coinChange(coins,amount):
    ans = solve(coins,amount)
    if ans == float('inf'):
        return -1
    return 

coins = [1,2,5]
amount = 11
# coins = [2]
# amount = 3

ans = coinChange(coins,amount)
print("Minimum Coins To Make an Amount is : ",ans)