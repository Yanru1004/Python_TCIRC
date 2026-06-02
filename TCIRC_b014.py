#b014 串串的三角形

#讀取三邊長

a,b,c = map(int,input().split(' '))

x = a**2 + b**2
y = c**2

if a + b <= c:
    print('NULL')

elif x > y:
    print('Acute Triangle')

elif x == y:
    print('Right Triangle') 

elif x < y:
    print('Obtuse Triangle')

else:
    print('Error')