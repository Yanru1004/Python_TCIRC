#b001 電電的強迫症

#讀入兩數

a,b = map(int,input().split())

while b >= 1:
    a,b = b,a%b

print(a)