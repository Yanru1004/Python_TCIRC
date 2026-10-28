#z043. 吃午餐要排隊

def check(num,day,line):
    #創建順位
    order = [i for i in range(day,num+1)] + [i for i in range(1,day)]
    buffer = []

    for turn in order:
        #print(f'{turn} time')
        while not len(buffer) or buffer[-1] != turn:
            if len(line) != 0:
                buffer.append(line[0])
                line = line[1:]
                #print(buffer)
            else:
                return 'No'
                

        buffer = buffer[0:-1]
        #print(buffer)
    else:
        return 'Yes'
    
    

num = int(input())

for day in range(1,num+1):
    line_ = [int(i)for i in input().split()]

    print(check(num,day,line_))