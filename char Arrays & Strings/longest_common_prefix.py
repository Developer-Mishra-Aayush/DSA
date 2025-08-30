"""
Title: Longest Common Prefix
Approach: Sort strings; common prefix of first and last after sort equals overall LCP.
Time: O(n log n + L)
Space: O(1)
"""

def longestCommonPrefix(strs):
    strs = sorted(strs)
    first = strs[0]
    end = strs[-1]
    length = min(len(first),len(end))
    i = 0
    ans = ""
    while i<length:
        if first[i]==end[i]:
            ans+=first[i]
        else:
            return ans
        i+=1
    return ans

strs = ["flower","flow","flight"]
ans = longestCommonPrefix(strs)
print("Longest Common Preifx is : ",ans)