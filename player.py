from game import Player, Board, Simulator
import sys

class Solver(Player):
    def __init__(self):
        self.game=[0,0,1]
        self.move=[{},{},{0:0}]
        
    def _game_value(self,n):
        while(n>=len(self.game)):
            k=len(self.game)
            s={}
            for i in range((k-2)//2+1):
                s[self.game[i]^self.game[k-2-i]]=i
            g=0
            new_s={}
            while(g in s):
                new_s[g]=s[g]
                g+=1
            self.game.append(g)
            self.move.append(new_s)
        return self.game[n]

    def _number_of_digits(n):
        i=0
        while(n):
            n=n>>1
            i+=1
        return i

    def _get_kth_digit(n,k):
        assert (k>0)
        while(k>1):
            n=n>>1
            k-=1
        return n%2
        
    def program(self,board):
        xorsum=0
        for g in board.state:
            xorsum=xorsum^self._game_value(g)
        if xorsum==0:
            return 'Resign'
        else:
            k=Solver._number_of_digits(xorsum)
            i=0
            for g in board.state:
                val=self.game[g]
                if(Solver._get_kth_digit(val,k)):
                    val_new= val^xorsum
                    assert(val_new<val)
                    m=self.move[g][val_new]
                    return (i,m)
                i+=1
            assert(false)
            
def main():
    solver = Solver()
    manual = Player()
    n = 17
    if(len(sys.argv)>1):
        n=int(sys.argv[1]);
    # Start simulator on Circle with 10 points with solver as player 0
    # manual (you) as player 1.
    sim = Simulator(Board.from_circle(n),solver,manual)
    print("Starting simulation on circle with <0> points. The computer is\
 playing first!\n")
    while(sim.step()): pass;
    input()

if (__name__ == "__main__"):
    main()
