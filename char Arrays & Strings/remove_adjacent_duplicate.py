def removeDuplicates(s):
    ans = []
    for i in s:
        if not ans:
            ans.append(i)
        elif ans[-1]==i:
            ans.pop()
        else:
            ans.append(i)
    return ''.join(ans)



s = input("Enter the String : ")
ans = removeDuplicates(s)
print("After removing Duplictes : ",ans)