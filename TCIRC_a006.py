#a006 勘根定理

#讀取各項係數

a,b,c,d,e,f = list(map(int,input().split(' ')))

#定義計算函數
def func(x):
    return a * (x**5) +b * (x**4) +c * (x**3) +d * (x**2) +e *x +f

if not any([a,b,c,d,e,f]):
    print('Too many... = ="')

else:
    sign = -2
    no_ans = True
    for i in range(-35,36):
        
        if func(i) == 0:
            print(f'{i} {i}')
            no_ans = False
            sign = -2
        elif sign == -1 and func(i) >0:
            print(f'{i-1} {i}')
            no_ans = False
            sign = 1
        elif sign == 1  and func(i) <0:
            print(f'{i-1} {i}')
            no_ans = False
            sign = -1
        else:
            sign = (func(i)>0) + (func(i)<0)*(-1)
    if no_ans == True:
        print(r'N0THING! >\\<')
