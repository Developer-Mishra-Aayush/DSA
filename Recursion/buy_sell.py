"""
Title: Buy and Sell Stock
Approach: Use recursion to find the maximum profit by trying all possible buy and sell combinations
Time: O(2^n) where n is the number of days
Space: O(n) for recursion stack
"""

def maxProfit(nums):
    buy_price = nums[0]
    maxProfit = 0
    for i in range(1,len(nums)):
        if buy_price>nums[i]:
            buy_price = nums[i]
        else:
            maxProfit = max(maxProfit,nums[i]-buy_price)
    return maxProfit

nums = [7,1,5,3,6,4]
# nums = [7,6,4,3,1]
ans = maxProfit(nums)
print("Maximum Profit is :",ans)