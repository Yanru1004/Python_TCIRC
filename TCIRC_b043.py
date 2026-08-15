#b043 Queue

import queue

box = queue.Queue()

num = int(input())
result =[]

for i in range(num):
    command = input().split()
    if command[0] == 'PUSH':
        box.put(command[1])
    elif not box.empty() and command[0] == 'POP':
        result.append(box.get())
        box.task_done
        
print('\n'.join(result))