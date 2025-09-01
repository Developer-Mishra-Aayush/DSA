from collections import deque

def nextSmaller(nums):
    ans = [0 for _ in range(len(nums))]
    nSmaller  = deque()
    nSmaller.append(-1)
    for j in range(len(nums)-1,-1,-1):
        while nSmaller[-1]>=nums[j]:
            nSmaller.pop()
        ans[j] = nSmaller[-1]
        nSmaller.append(nums[j])
    return ans

nums = [8,4,6,2,3]
ans = nextSmaller(nums)
print("Next Smaller Element is : ",ans)