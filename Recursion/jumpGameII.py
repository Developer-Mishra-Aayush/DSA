"""
Title: Jump Game II (Greedy Minimum Jumps)
Approach: Greedy BFS-on-array: track current jump boundary (end) and farthest reach (maxReach); when i reaches end, increment jumps and extend end to maxReach
Time: O(n)
Space: O(1)
"""

def minJump(nums):
    n = len(nums)
    if n <= 1:
        return 0

    maxReach = 0   # farthest reachable
    step = 0       # number of jumps
    end = 0        # end of current jump

    for i in range(n-1):  # last index doesn't need jump
        maxReach = max(maxReach, i + nums[i])

        # If we reached the end of current jump
        if i == end:
            step += 1
            end = maxReach

        # If current maxReach cannot progress
        if maxReach <= i:
            return -1  # cannot reach end

    return step


nums = [4, 3, 1, 1, 4]
ans = minJump(nums)
print("Minimum Jump to Reach End:", ans)
