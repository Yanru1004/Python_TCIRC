#a025 文文的求婚--續集 (n 行版)

num = int(input())

for i in range(num):
    year = int(input())

    if year%4 == 0 and year%100 != 0 or year%400 ==0:
        print('a leap year')
    else:
        print('a normal year')
