#b035 電皇的資源回收場

_ = int(input())

item = [int(x) for x in input().split()]

value = int(input())
result = 0

for i in range(0,len(item)-1):
    for j in range(i+1,len(item)):
        if item[i] + item[j] == value:
            result += 1

print(result)


