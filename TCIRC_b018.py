#b018 可樂成癮患者

#讀取可樂瓶數
x,y = map(int,input().split())

#初始化飲用數及瓶蓋數
result,cap = 0,0

#喝光纖維可樂換正常可樂
result += y
x += (y//3)

#喝光正常可樂
result += x
cap += x

#換可樂及飲用
while cap >= 5:
    new_cola = (cap //5)
    result += new_cola
    cap = (cap %5) + new_cola

print(result)
