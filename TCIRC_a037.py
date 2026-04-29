#a037 我也愛偶數 (swap 版)

#讀取a,b
a,b = list(map(int,input().split(' ')))

if a > b:
    a,b = b,a

result = 0

for i in range(a,b+1):
    if i%2 == 0:
        result += i

print(result)