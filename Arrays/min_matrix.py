def minimumMatrix(nums):
    max = float('inf')
    for i in nums:
        mini = min(max,min(i))
    return mini

nums = [[70,23,41],
        [27,69,42],
        [56,12,18]]

min = minimumMatrix(nums)
print("Minimum In Matrix is : ",min)