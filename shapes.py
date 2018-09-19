x=1 #kindoff to lazy to make the appropriate one :D
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


x = 0

y = int(input("Input another number:"))

while x < y:

    x += 1

    print(" " * (y-x) + "*" * x + "*" * (x-1) + " " * (y-x+1))



x = 0

y = int(input("Input another number:"))

z = 0

while x < y:

    x += 1

    print(" " * (y-x) + "*" * x + "*" * (x-1))

    while x == y:

        z += 1

        print(" " * z + "*" * (y-z) + "*" * (y-z-1))

        if z == y:

            break



