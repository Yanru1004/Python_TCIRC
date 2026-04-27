#a027 文文的求婚--續集 (EOF 版)

while True:
    try:
        year = int(input())

        if year == 0:
            break

        if year%4 == 0 and year%100 != 0 or year%400 ==0:
            print('a leap year')
        else:
            print('a normal year')
    
    except:
        break