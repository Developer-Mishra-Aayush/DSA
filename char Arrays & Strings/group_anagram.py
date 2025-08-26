"""
Title: Group Anagrams (Naive)
Approach: Repeatedly pick a word and collect anagrams by comparing sorted characters; remove as you go.
Time: O(n^2 * L log L)
Space: O(n)
"""

def groupAnagram(strs):
    ans = []
    while strs:
        tempAns = []
        first = strs.pop(0)
        tempAns.append(first)
        for i,data in enumerate(strs[:]):
            if sorted(data)==sorted(first):
                tempAns.append(data)
                ss = strs.remove(data)
                print("Removed String is : ",ss)
        ans.append(tempAns)
    return ans

strs = ['eat','tea','tan','ate','nat','bat']
strs = ["","",""]
ans = groupAnagram(strs)
print("Group Anagram is : ",ans)