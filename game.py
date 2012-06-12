#
#
#
class Board:
    def __init__(self,l=[]):
        self.state=[]
        for i in l:
            if(i>0):
                self.state.append(i)
        self.state.sort()

    def __str__(self):
        ans=""
        for i in range(len(self.state)):
            ans=ans+"{0}:{1}, ".format(i,self.state[i])
        return ans[:-2]

    def from_circle(n):
        return Board([n])

    def move(self,m):
        k,i=m
        if (k>=0 and k<len(self.state)):
            if(i>=0 and i<=self.state[k]-2):
                if(i==self.state[k]-2):
                    self.state.pop(k)
                else:
                    self.state[k]=self.state[k]-2-i
                if(i>0):
                    self.state.append(i)
                self.state.sort()
            else:
                raise Exception("Invalid move!")
        else:
            raise Exception("Invalid move!")

    def isfinished(self):
        for i in self.state:
            if i>1:
                return False
        return True

class Player:
    def __init__(self):
        def program(board):
            while(True):
                print('Your move? Enter h for help.')
                inp=input()
                if(inp=='Resign'):
                    return inp
                if(inp=='h'):
                    print ("To split i^th block of points to two blocks having\
 k and n_i-k-2 points, enter: i k")
                    print ("Otherwise,'Resign' to accept defeat.")
                    continue
                try: i,k=inp.split()
                except ValueError:
                    print("Invalid input!")
                    continue

                i=int(i)
                k=int(k)

                return (i,k)

        self.program=program

class Simulator:
    def __init__(self,b,player0,player1):
        self.board=b
        self.p=[player0,player1]
        self.move=0
    
    def step(self):
        print('The state is\n '+str(self.board)+'\n')
        while(True):
            ch=self.p[self.move].program(self.board)
            if (ch=='Resign'):
                print('Player {0} accepts defeat!!\n'.format(self.move))
                return 0
            try :
                self.board.move(ch)
                print('Player {0} makes move {1}\n'.format(self.move,ch))
                break
            except Exception as instr:
                print(instr)
        if self.board.isfinished():
            print('No more moves left for Player {1}! Player {0} wins!!'.format(self.move,1-self.move))
            return 0
        self.move^=1
        return 1
