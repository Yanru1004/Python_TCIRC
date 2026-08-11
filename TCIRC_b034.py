#b034 Arvin 拉麵店

#匯入序列模組

task = []

while True:
    command = input().split()

    if command[0] == 'INSERT':
        task.append(int(command[1]))

    elif command[0] == "POP_LARGE":
        if len(task) == 0:
            print("Nothing To Do :)")
        else:
            n = max(task)
            print(n)
            task.remove(n)

    elif command[0] == "POP_SMALL":
        if len(task) == 0:
            print("Nothing To Do :)")
        else:
            n = min(task)
            print(n)
            task.remove(n)
    elif command[0] == "END":
        break
