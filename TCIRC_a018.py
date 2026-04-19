# a018. 還要等多久啊？

#讀取目前時間分
minute = int(input())

result = (25 - minute + 60) % 60

print(result)

