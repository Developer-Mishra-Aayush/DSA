def removeDuplicates(s,k):
    new_s = []
    if len(s)<k:
        return s
    
    for i in range(len(s)):
        print("Current i is : ",s[i])
        # if new_s and new_s[-1][1]==k:
        #     temp = k
        #     while temp:
        #         temp-=1
        #         a = new_s.pop()
        #         print("Popped Element is : ",a)
        if not new_s:
            new_s.append([s[i],1])
            print("New list is : ",new_s)
        elif s[i]==new_s[-1][0]:
            if new_s[-1][1] == k-1:
                temp = k - 1
                while temp:
                    temp-=1
                    a = new_s.pop()
                    print("Popped Element is : ",a)
            else:
                new_s.append([s[i],new_s[-1][1]+1])
                print("New lists is : ",new_s)
        else:
            new_s.append([s[i],1])
            print("News list is : ",new_s)
    ans = ""
    for i in new_s:
        ans+=i[0]
    return ans



s = input("Enter the String : ")
k = int(input("Enter the K : "))
ans = removeDuplicates(s,k)
print("After Removing K Adjacent Duplicates : ",ans)