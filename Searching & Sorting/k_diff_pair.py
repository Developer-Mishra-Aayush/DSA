"""
Title: K-diff Pairs in an Array
Approach: Use a set to track seen numbers and add valid pairs (num-k, num) or (num, num+k) into an output set to dedupe.
Time: O(n)
Space: O(n)
"""

def findPairs(nums,k):
    seen = set()
    output = set()
    for num in nums:
        if num + k in seen:
            output.add((num,num+k))
        if num - k in seen:
            output.add((num-k,num))
        seen.add(num)
    return len(output)

# nums = [3,1,4,1,5]
# k = 2
nums = [1,2,3,4,5]
k = 1

ans = findPairs(nums,k)
print("Total Pair is : ",ans)