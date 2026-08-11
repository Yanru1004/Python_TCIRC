#b022 質數惡夢

#讀取正整數

M = int(input())

n = 2
prime_number = []

while n  < M:
    is_prime = True
    for pn in prime_number:
        
        if pn * pn > n:
            break

        if n % pn == 0:
            is_prime = False
            break
    
    if is_prime == True:
        prime_number.append(n)

    n += 1

print(' '.join(map(str,prime_number)))
