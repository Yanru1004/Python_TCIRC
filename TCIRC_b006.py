#b006 電電的梯形

#讀取上底、下底、高

t,b,h = map(int,input().split(' '))

area = ((t+b)*h)//2

print(area)