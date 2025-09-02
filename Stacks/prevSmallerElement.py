"""
Title: Previous Smaller Element
Approach: Traverse left to right maintaining a monotonic increasing stack; for each element, pop until smaller is found
Time: O(n)
Space: O(n)
"""

from collections import deque

def prevSmaller(nums):
    ans = [0 for _ in range(len(nums))]
    pSmaller  = deque()
    pSmaller.append(-1)
    for j in range(len(nums)):
        while pSmaller[-1]>=nums[j]:
            pSmaller.pop()
        ans[j] = pSmaller[-1]
        pSmaller.append(nums[j])
    return ans

nums = [8,4,2,6,3]
ans = prevSmaller(nums)
print("Next Smaller Element is : ",ans)