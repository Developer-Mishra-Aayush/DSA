"""
Title: Group Anagrams (Optimized)
Approach: Use sorted string as key in a dictionary to group anagrams.
Time: O(n * L log L)
Space: O(n * L)
"""

def groupAnagram(strs):
    dict = {}
    for i in strs:
        ans = ''.join(sorted(i))
        if ans in dict:
            dict[ans].append(i)
        else:
            dict[ans] = [i]
    ans = []
    for i in dict:
        ans.append(dict[i])
    return ans

strs = ['eat','tea','tan','ate','nat','bat']
ans = groupAnagram(strs)
print("Group Anagram is : ",ans)