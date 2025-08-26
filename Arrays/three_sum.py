"""
Title: Three Sum (Find unique triplets summing to zero)
Approach: Sort array, fix one element, and use two-pointer sweep to find pairs; store triplets in a set.
Time: O(n^2)
Space: O(k) for output set (ignoring sort), typically O(1) extra
"""

def threeSum(nums):
    if len(nums)<=2:
        return -1
    nums.sort()
    ans = set()
    for i in range(len(nums)-2):
        firstSum = nums[i]
        j = i+1
        k = len(nums)-1
        while j<k:
            secondSum = nums[j]
            thirdSum = nums[k]
            totalSum = firstSum + secondSum + thirdSum
            if totalSum ==0:
                ans.add((firstSum,secondSum,thirdSum))
                j+=1
                k-=1
            elif totalSum>0:
                k-=1
            else:
                j+=1
    return ans

nums = []
n = int(input("Enter the Size : "))
for i in range(n):
    element = int(input("Enter the Data : "))
    nums.append(element)

ans = threeSum(nums)
print("Three Sum is : ",ans)