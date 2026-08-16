#b040 鐵軌道岔

n,m = map(int,input().split())

def check(ask:list):
    #初始化
    rail_a_head = 0
    station = []

    for b in ask:
        if rail_a_head > n:
            return 'No'
        
        if rail_a_head == b:
            rail_a_head += 1 #直接進rail_b
            
        elif rail_a_head < b:
            #目標車廂還在鐵軌A
            while rail_a_head < b:
                station.append(rail_a_head)
                
                rail_a_head += 1
            #目標車廂至鐵軌A開頭，直接進rail_b
            rail_a_head += 1

        else:
            #目標車廂已離開鐵軌A，去車站找。
            
            if station and station[-1] == b:
                station.pop()
            else:
                return 'No'
    
    return 'Yes'

for ask in range(m):
    li = [int(x) for x in input().split()]
    print(check(li))