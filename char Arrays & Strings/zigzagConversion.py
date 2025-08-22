def convert(s,numRows):
    ans = []
    for i in range(numRows):
        ans.append([])
    i = 0
    start = -1
    while i<len(s):
        start+=1
        while i<len(s) and start<numRows:
            ans[start].append(s[i])
            i+=1
            start+=1
        start-=1
        while i<len(s) and start>0:
            start-=1
            ans[start].append(s[i])
            i+=1
    s = ""
    for i in ans:
        s+=''.join(i)
    return s

s = input("Enter the String :")
numRows = int(input("Enter the Rows"))
ans = convert(s,numRows)
print("After Converting into Zigzag :",ans)