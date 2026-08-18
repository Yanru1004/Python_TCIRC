#b038 存量問題

target_day = int(input())

#初始化
fee = [1,1,1]
day = 1
k_day = 1
k_banana = 0
banana = 0

while day <= target_day:

    #採收香蕉
    banana += 80
    #計算上繳香蕉
    if len(fee) <= k_day+2:
        fee.append(fee[k_day] + fee[k_day+1])

    #革命與否檢查
    if banana > fee[k_day]:
        banana -= fee[k_day]
        k_banana += (fee[k_day] * 20)
        
    else:
        
        k_banana += banana * 20
        banana = int((k_banana *0.95)//20)
        k_banana -= (banana*20)
        k_day = 0

    
    day += 1
    k_day += 1
    k_banana -= (k_banana)//2

print(banana)