#b044 卑鄙約瑟夫

n,k = map(int,input().split())

party = [x for x in range(n)]
ptr = 1

while len(party) > 1:
    new_party = []
    for p in party:
        if ptr < k:
            new_party.append(p)
            ptr += 1
        else:
            ptr = 1
    party = new_party

print(party[0])