def customSortString(order,s):
    ans = []
    order = list(order)
    s = list(s)
    len1 = len(order)
    len2 = len(s)
    i = 0
    while i<min(len1,len2):
        if order[i] in s:
            while order[i] in s:
                ans.append(order[i])
                s.remove(order[i])
        i+=1
    ans.extend(s)
    return ''.join(ans)

s = input("Enter the String : ")
t = input("Enter the String :")
ans = customSortString(s,t)
print("After Custom Sort String : ",ans)