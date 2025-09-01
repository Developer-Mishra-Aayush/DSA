"""
Title: Remove All Occurrences
Approach: Use recursion to remove all occurrences of a target element from the array
Time: O(n) where n is the length of the array
Space: O(n) for recursion stack
"""

def removeOccurence(s,part):
    if s.find(part)!=-1:
        s = s.replace(part,'')
        return removeOccurence(s,part)
    return s

s = "daabcbaabcbc"
part = "abc"
ans = removeOccurence(s,part)
print("After Removing All Occurence of Part From a String : ",ans)