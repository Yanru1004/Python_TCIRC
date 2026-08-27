#b034 Arvin 拉麵店

#匯入序列模組

import heapq

task_min = []
task_max = []
dic_cnt = {}

while True:
    command = input().split()

    if command[0] == 'INSERT':
        #填入數字
        num = command[1]
        heapq.heappush(task_max,-num)
        heapq.heappush(task_min,num)
        dic_cnt.setdefault(num,0)
        dic_cnt[num] += 1

    elif command[0] == 'POP_LARGE' and task_max and task_min:
        pop_num = -task_max[0]
        


