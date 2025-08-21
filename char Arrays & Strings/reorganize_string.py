def reorganize(s):
    s = list(s)
    # Find the Max Occuring String
    dict = {}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
    maxOccurence = 0
    maxString = ''
    for i in dict:
        if dict[i]>maxOccurence:
            maxOccurence = dict[i]
            maxString = i
    
    # Now try to place the maxString in Even Position
    index = 0
    while maxOccurence and index <len(s):
        s[index] = maxString
        maxOccurence-=1
        index+=2
    if maxOccurence!=0:
        return ""
    dict[maxString] = 0

    for i in dict:
        if dict[i]!=0:
            while dict[i]:
                if index+2>=len(s):
                    index = 1
                else:
                    index+=2
                s[index] = i
                dict[i]-=1
    return ''.join(s)

s = input("Enter the String : ")
ans = reorganize(s)
print("After Reorganize String : ",ans)