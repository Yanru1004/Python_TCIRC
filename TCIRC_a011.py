#a011 加減乘除

while True:
    try:

        #讀入算式
        a,op,b = input().split(' ')

        if op == '+':
            print(int(a)+int(b))
        elif op == '-':
            print(int(a)-int(b))
        elif op == '*':
            print(int(a)*int(b))
        elif op == '/':
            print(int(a)//int(b))
        else:
            print('error')

    except:
        break
