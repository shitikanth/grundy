SOLVER FOR IMPARTIAL GAMES
==========================

The aim of this module is to implement a generic solver
for impartial games like NIM.

Please refer to the links at the bottom of this page for 
some good lecture notes on the beautiful theory of impartial
games.

For the purpose of this module, we need two results:
1.  Every game is equivalent to some NIM game. This relationship
    is given by the Grundy number (also called nimber) of the game.
    If G_1 to G_k are the games reachable from G,
    g(G) = mex({g(G_1),...,g(G_k)})
    mex of a set of integers is defined to be the smallest non-negative
    integer not in that set.
2.  If G and H are two games, their sum G+H is defined as the game
    where the two games are to be played simultaneously, i.e., 
    in her turn, the player will have to choose one of the games
    G or H and make one move in that game.


REMARKS
--------
The code is very far from the goal of being a generic solver. I will
get around to writing it when I have the time.

Right now, I have made a solver for a specific impartial game 
suggested by a friend.

> N points are chosen around a circle. Now Bob and Alice play the following game:
> Alice draws a line connecting two of the points with a line segment. 
> Bob and Alice move in turn, but the line segment cannot cross any of the 
> previously drawn lines (the end points cannot even be reused).
> A player who cannot draw a suitable line loses.

USAGE
------
To play the game as Bob (computer plays first), do 
`python player.py N`
where N is the number of points on the circle.

To see the first N grundy values of the game, do
`python circlegame.py`

I have included windows 32 bit exectubles for player and circlegame 
in the dist directory.

P.S. I have no rights to distribute msvcm90.dll, msvcp90.dll, msvcr90.dll

REFERENCES
[www.math.ucla.edu/~tom/Game_Theory/comb.pdf]
[web.mit.edu/sp.268/www/nim.pdf]
