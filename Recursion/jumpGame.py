"""
Title: Jump Game (Greedy)
Approach: Iterate from right to left maintaining the last good index (goal). If i + nums[i] >= goal, update goal to i. Reachable if goal reaches 0
Time: O(n)
Space: O(1)
"""

def canJump(nums):
    goal = len(nums)-1
    for i in range(len(nums)-2,-1,-1):
        if nums[i]+i>=goal:
            goal = i
    return goal==0



nums = [2,3,1,1,4]
ans = canJump(nums)
print("Is able to Jump to Last Element : ",ans)