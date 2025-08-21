def compress(chars):
    dict = {}
    for i in chars:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
    ans = ""
    for i in dict:
        ans+=i
        if dict[i]!=1:
            ans+=str(dict[i])
    return list(ans)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# chars = ["a","a","b","b","c","c","c"]
ans = compress(chars)
print("Compress Ans : ",ans)