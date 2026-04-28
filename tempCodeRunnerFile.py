#a034 我愛偶數

#讀取a,b
a,b = list(map(int,input().split(' ')))
           
print((b-a)//2+(a%2==0))