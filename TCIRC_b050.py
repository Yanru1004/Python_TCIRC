#b050 愛吃拉麵的小暘教授

class jobs():
    def __init__(self,start,end,money):
        self.start = start
        self.end   = end
        self.money = money

    def __

task = []
num=int(input())

for i in range(num):
    data = map(int,input().split())
    task.append(jobs(*data))

print(task[0].start)
