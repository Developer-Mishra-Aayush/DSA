"""
Title: Number of Dice Rolls With Target Sum
Approach: Use recursion with memoization to count all possible ways to roll dice to reach target sum
Time: O(n * k * target) where n is number of dice, k is faces per die, target is the target sum
Space: O(n * target) for recursion stack and memoization
"""

def solve(n,k,target):
    if target<0:
        return 0
    if n ==0 and target==0:
        return 1
    if n!=0 and target==0:
        return 0
    if n==0 and target!=0:
        return 0
    else:
        ans = 0
        for i in range(1,k+1):
            ans = ans + solve(n-1,k,target-i)
        return ans

def numRollsToTarget(n,k,target):
    ans = solve(n,k,target)
    return 

n = 1
k = 6
target = 3
ans = numRollsToTarget(n,k,target)
print("All Possibel Number of Dice Throws To make a Target is : ",ans)