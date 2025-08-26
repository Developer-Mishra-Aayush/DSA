"""
Title: Remove All Adjacent Duplicates in String II (k duplicates)
Approach: Maintain a stack of [char, count]; when count reaches k-1 and next is same, pop k-1 entries, otherwise push with incremented count.
Time: O(n)
Space: O(n)
"""

def removeDuplicates(s,k):
    new_s = []
    if len(s)<k:
        return s
    
    for i in range(len(s)):
        if not new_s:
            new_s.append([s[i],1])
        elif s[i]==new_s[-1][0]:
            if new_s[-1][1] == k-1:
                temp = k - 1
                while temp:
                    temp-=1
                    a = new_s.pop()
            else:
                new_s.append([s[i],new_s[-1][1]+1])
        else:
            new_s.append([s[i],1])
    ans = ""
    for i in new_s:
        ans+=i[0]
    return ans

s = input("Enter the String : ")
k = int(input("Enter the K : "))

ans = removeDuplicates(s,k)
print("After Removing K Adjacent Duplicates : ",ans)