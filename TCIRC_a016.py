#a016. 糟糕，我發燒了！

def f_to_c(f):
    c = (f-32)*(5/9)
    return c

f_temp = int(input())
print(f'{f_to_c(f_temp):0.3f}')
