#b045 Priority Queue 模板題

import heapq

num = int(input())

h = []
result = []

for i in range(num):
    command = input().split()

    if command[0] == 'PUSH':
        heapq.heappush(h,int(command[1])*-1)

    else:
        if len(h) != 0:
          result.append(h[0]*-1)
          heapq.heappop(h)

print('\n'.join(map(str,result)))