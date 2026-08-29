#b052 減法遊戲

_ = input()

li = [int(x) for x in input().split()]

max_num = li[0]
pre_result = li[0]

for i in range(1,len(li)):

    new_result = max(pre_result - li[i],li[i])
    pre_result = (new_result)
    if pre_result > max_num:
        max_num = pre_result

print(max_num)