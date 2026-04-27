#文文的求婚--續集 (Case 版)

num = int(input())

for i in range(num):
    year = int(input())

    print(f'Case {i+1}: ',end='')

    if year%4 == 0 and year%100 != 0 or year%400 ==0:
        print('a leap year')
    else:
        print('a normal year')
