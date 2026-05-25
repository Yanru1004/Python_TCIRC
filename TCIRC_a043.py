#a043 棄保效應

#讀取支持者數

a,b,c = map(int,input().split(' '))

if a >= b+c:
    print('A')

elif b= > a+c:
    print("B")

elif c >= a+b:
    print("C")

elif a > b and a >c:
    if b > c:
        print("B")
    else:
        print("C")
elif b > a and b > c:
    if a > c:
        print("A")
    else:
        print("C")
elif c > a and c >b:
    if a > b:
        print("A")
    else:
        print("B")

    
