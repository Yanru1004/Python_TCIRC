#a004. 經濟大恐慌

#初始化
pay = 0
price = 1

#讀取購買天數
day = int(input())
#讀取每日購買數量
quantity = map(int,input().split(' '))

for q in quantity:
    pay += (price * q)
    price += 1

print(pay)