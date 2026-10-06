#b057. 古老的審判

class game():
    def __init__(self):
        self.beard = [['.' for y in range(3)] for x in range(3)]

    def show_beard(self):
        for i in self.beard:
            for j in i:
                print(j,end=' ')
            print('')

    def put_token(self,pos,round):
        if (pos[0] not in [1,2,3]
            or pos[1] not in [1,2,3]
            or self.beard[pos[0]-1][pos[1]-1] != '.'):

            print('Illegal!')
            return round
            
        else:
            self.beard[pos[0]-1][pos[1]-1] = ['X','O'][(round%2)]            
            return round + 1

    def check(self):
        end_game = False
        check_list = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for li in check_list:
            if (self.beard[li[0]//3][li[0]%3] == self.beard[li[1]//3][li[1]%3]
                and self.beard[li[0]//3][li[0]%3] == self.beard[li[2]//3][li[2]%3]
                and self.beard[li[0]//3][li[0]%3] != '.'):
                end_game = True
                return end_game
                
            

new_game = game()

round = 1
while round <10: 
    new_game.show_beard()
    print(f"{['God','Human'][round%2]}'s turn!")

    now_round = round
    while now_round == round:
        pos = [int(x) for x in input().split()]
        round = new_game.put_token(pos,round)    
    end_game = new_game.check()
    if end_game:
        round -= 1
        print(f"{['God','Human'][round%2]} wins!")
        break
else:
    print("Tie")