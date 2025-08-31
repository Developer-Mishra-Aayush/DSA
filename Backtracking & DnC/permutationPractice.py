def solve(nums, ans, index):
    if index >= len(nums):
        ans.append(nums[:])
        return
    
    seen = set()
    for j in range(index, len(nums)):
        if nums[j] in seen:   # skip duplicate choice
            continue
        seen.add(nums[j])
        nums[index], nums[j] = nums[j], nums[index]
        solve(nums, ans, index+1)
        nums[index], nums[j] = nums[j], nums[index]  # backtrack

def permutation(nums):
    ans = []
    solve(nums, ans, 0)
    return ans

nums = [1,1,2]
ans = permutation(nums)
print("Unique Permutations:", ans)