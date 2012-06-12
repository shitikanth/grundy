import grundy

game=[0,0,1]

def game_value(n):
    while(n>=len(game)):
        k=len(game)
        s=set()
        for i in range ((k-2)//2+1):
            s.add(game[i]^game[k-2-i])
        game.append(grundy.mex(s))
    print(game)
    return (game[n])

def main():
    n=int(input("Enter n: "))
    print("The first n grundy values of the circle game are:")
    game_value(n)
    input()

if __name__ == "__main__":
    main()
