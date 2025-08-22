def intToRoman(num):
    numeral = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    literal = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    i = 0
    ans = ""
    while num!=0 and i<len(numeral):
        while num>=numeral[i]:
            num-=numeral[i]
            ans+=literal[i]
        i+=1
    return ans

num = int(input("Enter the Number : "))
ans = intToRoman(num)
print("Integer to Roman is : ",ans)