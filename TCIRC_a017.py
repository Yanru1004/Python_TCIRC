#a.017 BASIC的SGN函數

def sqn(x):
    return -(x<0)+(x>0)

print(sqn(int(input())))