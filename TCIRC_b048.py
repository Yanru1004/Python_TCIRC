#b048 y=a+b

n,y = map(int,input().split())

li = [int(x) for x in input().split()]

head,tail = 0,len(li)-1
have_sol = False

while True:

    calc = li[head] + li[tail]

    if calc == y:
        have_sol = True
        break
    elif calc > y:
        tail -= 1

    elif calc < y:
        head += 1

    if head == tail:
        print("IMPOSSIBLE")
        break

if have_sol:
    print(head,tail)
    
