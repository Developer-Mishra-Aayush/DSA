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