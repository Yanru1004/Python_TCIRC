#b021 電電找因數

#讀入資訊

while True:
    try:
        n = int(input())

        num = []       
        for i in range(1,n+1):
            if n % i == 0:                
                num.append(str(i))
                
        result = ' '.join(num)
        print(result)     

    except:
        break