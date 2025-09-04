"""
Title: Sliding Window Maximum
Approach: Maintain a deque of indices with decreasing values; front holds max for the current window
Time: O(n)
Space: O(k)
"""

from collections import deque

def maxSlidingWindow(nums,k):
    stack = deque()
    ans = []
    # Iterate for first window
    for i in range(k):
        while  stack and nums[stack[-1]]<nums[i]:
            stack.pop()
        stack.append(i)
    # Store the First Answer in Ans List
    ans.append(nums[stack[0]])

    # Now Handle all the Remaining Window
    for i in range(k,len(nums)):
        # Remove the Less Index ELement from the stack
        while stack and stack[0]<i-k+1:
            stack.popleft()
        # Now remove the smaller Element From the stack from right side
        while stack and nums[stack[-1]]<nums[i]:
            stack.pop()
        stack.append(i)
        ans.append(nums[stack[0]])
    return ans
        

nums = [1,3,-1,-3,5,3,6,7]
k = 3
ans = maxSlidingWindow(nums,k)
print("Maximum SLoding Window Array is : ",ans)