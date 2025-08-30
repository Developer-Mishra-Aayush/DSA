"""
Title: Rotate Image (Matrix) 90° Clockwise
Approach: Transpose the matrix in-place, then reverse each row.
Time: O(n^2)
Space: O(1)
"""

def rotateImage(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums[0])):
            nums[i][j],nums[j][i] = nums[j][i],nums[i][j]
    for i in nums:
        i.reverse()
    return nums
    
nums = [[1,2,3],
        [4,5,6],
        [7,8,9]]

ans = rotateImage(nums)
print("After Rotating Image : ",ans)