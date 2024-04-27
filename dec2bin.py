val=eval(input("Enter a decimal number: "))
num=val
res=0
for i in range(8,-1,-1):
    if 2**i<=val:
        num=num-2**i
        if num<0:
            q=0
        else:
            q=1
        res=(res*10)+(1*q) 
    else:
        continue
print(f"Binary form: {res}")