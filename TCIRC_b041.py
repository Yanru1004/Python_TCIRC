#b041 括弧配對

def check(s:str):
    box = []
    pair_dict = {'>':'<',
                 ')':'(',
                 ']':'[',
                 '}':'{'}
    
    for sy in s:
        if sy in ['<','(','[','{']:
            box.append(sy)
        elif box != [] and box[-1] == pair_dict[sy]:
            box.pop()
        else:
            return 'F'
    return 'T' if box == [] else 'F'

result = []
while True:
    try:
        s = input()
        result.append(check(s))
    except:
        break

print('\n'.join(result))