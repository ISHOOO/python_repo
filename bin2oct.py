def bin2dec(n):
    x=0
    sum=0
    while(n):
        rem=n%10
        n=n//10
        sum+=rem<<x
        x+=1
    return sum
num=eval(input("Enter a binary number:"))
i=0
res=0
while(num):
    r=num%1000
    num=num//1000
    res+=bin2dec(r)*(10**i)
    i+=1
print(f"octal representation: {res}")