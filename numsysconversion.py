def dec2bin(dec):
    num=dec
    res=0
    for i in range(8,-1,-1):
        if 2**i<=dec:
            num=num-2**i
            q=num>=0
            res=(res*10)+(1*q) 
    return res

def bin2dec(bin_num):
    x,sum=0
    while(bin_num):
        rem=bin_num%10
        bin_num=bin_num//10
        sum+=rem<<x
        x+=1
    return sum

def bin2oct(bin_num):
    i,res=0
    while(bin_num):
        r=bin_num%1000
        bin_num=bin_num//1000
        res+=bin2dec(r)*10**i
        i+=1
    return res