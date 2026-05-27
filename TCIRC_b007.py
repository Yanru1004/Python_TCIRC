#b007 邊緣的串串

#讀入總人數m,分組人數n

m,n = map(int,input().strip().split(' '))

while m > n:
    m -= n

print(m)
