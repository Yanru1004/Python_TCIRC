#b035 電皇的資源回收場

from collections import Counter

_ = int(input())

item = [int(x) for x in input().split()]
value = int(input())

result = 0
cnt = Counter(item)
value_list = sorted(cnt.keys())
ptr_l,ptr_r = 0,len(value_list)-1

while True:
    add_value = value_list[ptr_l] + value_list[ptr_r]
    
    if add_value < value:
        ptr_l += 1
    elif add_value > value:    
        ptr_r -= 1    
    else:
        if ptr_l != ptr_r:
            result += cnt[value_list[ptr_l]] * cnt[value_list[ptr_r]]
           
            ptr_l += 1
        else:
            if value_list[ptr_l]*2 == value and cnt[value_list[ptr_l]]>1:
                result += cnt[value_list[ptr_l]]
                
            break

print(result)
