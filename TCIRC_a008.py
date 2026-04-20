#a008. 盈虧互補

#輸出真因數函數
def pd(num):
    sum = 1
    n = 2

    while n ** 2 < num:
        if num % n == 0:
            sum += (n + num//n)
        n += 1
    
    return sum

num = int(input())

while num !=0:
    if num == pd(num):
        print(f'={num}')
    
    elif num == pd(pd(num)):
        print(f'{pd(num)}')
    
    else:
        print(0)
    
    num = int(input())

    