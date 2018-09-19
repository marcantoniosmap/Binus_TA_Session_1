x=1
while x<6:
    print("*****")
    x=x+1

y=1
while y<6:
    print(y*"*")
    y=y+1


n=1
while n<6:
    x=6-n
    print(x*" ", n*"*")
    n=n+1

k=5
while k>0:
    l=5-k
    print( k*"*",l*" ")
    k=k-1

f=5
while f>0:
    d=5-f
    print(d*" ", f*"*")
    f=f-1


lk = 0
yk = 5
while lk < yk:
    lk += 1
    print(" " * (yk-lk) + "*" * lk + "*" * (lk-1) + " " * (yk-lk+1))



mn = 0
yy = 5
zz= 0

while mn < yy:
    mn += 1
    print(" " * (yy-mn) + "*" * mn + "*" * (mn-1))
    while mn == yy:
        zz += 1
        print(" " * z + "*" * (yy-zz) + "*" * (yy-zz-1))
        if zz == yy:
            break


