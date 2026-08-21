#b046 加法的成本

import heapq

_ = int(input())
result = 0
h = [int(x) for x in input().split()]
heapq.heapify(h)

while len(h) >= 2:
    num1 = heapq.heappop(h)
    num2 = heapq.heappop(h)
    cost = num1 + num2
    result += cost
    heapq.heappush(h,cost)

print(result)

