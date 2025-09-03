from collections import deque
def firstNegEveryK(nums,k):
    stack = deque()
    ans = []
    for i in range(0,k):
        if nums[i]<0:
            stack.append(i)
    for i in range(k,len(nums)):
        if not stack:
            ans.append(0)
        else:
            index = stack[0]
            ans.append(nums[index])
        # Now Remove the Negative index from the stack that are not the part of next range
        if stack and stack[0]<=i-k:
            print("Popping Index : ",stack[0])
            stack.popleft()
        # Add New Element
        if nums[i]<0:
            stack.append(i)
    if stack:
        ans.append(nums[stack[0]])
    else:
        ans.append(0)
    return ans

nums = [-8,2,3,-6,10]
k = 2
ans = firstNegEveryK(nums,k)
print("First Negative Element in Every K Window : ",ans)
