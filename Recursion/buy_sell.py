"""
Title: Best Time to Buy and Sell Stock (Single Transaction)
Approach: One pass tracking minimum price so far and maximum profit difference
Time: O(n)
Space: O(1)
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