#a035 伏林的三角地

#讀取三邊長
a,b,c = list(map(int,input().split(' ')))

#使用海龍公式

s = (a+b+c)/2

#題目要求平方，故不開根號
area = int(s*(s-a)*(s-b)*(s-c))

print(area)