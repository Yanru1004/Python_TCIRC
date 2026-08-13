#b039 Stack 模板題
import sys
input = sys.stdin.readline

num = int(input())

stack = []
result = []

for i in range(num):
    command= input().split()

    if command[0] == "PUSH":
        stack.append(command[1])

    elif command[0] == "POP":
        if len(stack):
            result.append(stack.pop())

print('\n'.join(result))

