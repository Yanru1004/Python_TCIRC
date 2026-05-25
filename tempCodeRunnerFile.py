#a041 奇怪的老闆

#讀取人數及問題數

person,question = list(map(int,input().split(' ')))

#讀取薪資資料
money = [50001]

for i in range(person):
    money.append(int(input()))

#問答開始
for q in range(question):

    #取得範圍
    a,b = list(map(int,input().split(' ')))

    diff = max(money[a:b]) - min(money[a:b])
    print(diff)
