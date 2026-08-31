#071. 電梯 (Elevator)

_ = input()

floor = [int(x) for x in input().split()]
pre_floor = 1
cost = 0

for i in floor:
    if i > pre_floor:
        cost += (i-pre_floor)*3
        pre_floor = i
    else:
        cost += (pre_floor-i) * 2
        pre_floor = i


print(cost)
