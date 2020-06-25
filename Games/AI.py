#game.moves()
#game.afterMove(move)
#game.score()

import math
from random import randint

tocan = 0

def scorer(game, bMove, x=0):
    game = game.afterMove(bMove)
    if game.moves() == []:
        print "bobobobobobobobobboobobobobobobobobob"
        return game.score()
    else:
        return -bestMoveAndScore(game, x)["score"]

def bestMoveAndScore(game, x=0):
    print x
    x+=1
    print game.x
    score = -2
    best_move = False
    for move in game.moves():
        move_score = scorer(game, move, x)
        if move_score > score:
            score = move_score
            best_move = move
    return {"move":best_move ,"score":score}




class Tic:


    def __init__(self, x=[]):
        self.x = x
        self.b = self.genB()


    def moves(self):
        if(len(self.x)>0):
            out = self.x[-1][1]
        else:
            out = 5;
        for i in self.b:
            if(i[0]==out):
                out = -1
        if(self.score()==-1 or self.score()==1):
            out = -2
        if(out == -2):
            return []
        elif(out!=-1):
            moves = []
            for option in self.x:
                if(option[0]==out):
                    moves.append(option[1])
            moves = set(moves)
            moves = list({1,2,3,4,5,6,7,8,9}-moves)
            final = []
            for i in moves:
                final.append([out, i])
            return final
        else:
            all_moves = []
            for t in range(1, 9):
                moves = []
                for option in self.x:
                    if(option[0]==t):
                        moves.append(option[1])
                moves = set(moves)
                moves = list({1,2,3,4,5,6,7,8,9}-moves)
                for i in moves:
                    all_moves.append([t, i])
            return all_moves


    def afterMove(self, cMove):
        new_x = self.x[:]
        if(len(new_x)%2==0):
            new_x.append(cMove+["x"])
        else:
            new_x.append(cMove+["o"])
        newGame = Tic(new_x)
        return newGame


    def score(self):
        w = [[],[],[],[],[],[],[],[]]
        for p in self.b:
            w[p[0]%3].append(p[1])
            w[int(math.ceil(p[0]/3.00)+2)].append(p[1])
            if(p[0]==1 or p[0]==5 or p[0]==9):
                w[6].append(p[1])
            if(p[0]==3 or p[0]==5 or p[0]==7):
                w[7].append(p[1])
        for p in w:
            total = 0
            for z in p:
                if(z=="x"):
                    total += 1
                else:
                    total-= 1
            if(total == 3):
                return -1
            elif(total == -3):
                return 1


    def genB(self):
        i = 1
        map = []
        while(i<=9):
            w = [[],[],[],[],[],[],[],[]]
            for p in self.x:
                if(p[0]==i):
                    w[p[1]%3].append(p[2])
                    w[int(math.ceil(p[1]/3.00)+2)].append(p[2])
                    if(p[1]==1 or p[1]==5 or p[1]==9):
                        w[6].append(p[2])
                    if(p[1]==3 or p[1]==5 or p[1]==7):
                        w[7].append(p[2])
            for p in w:
                total = 0
                for z in p:
                    if(z=="x"):
                        total += 1
                    else:
                        total-= 1
                if(total == 3):
                    map.append([i, "x"])
                    break
                elif(total == -3):
                    map.append([i, "o"])
                    break
            i+=1
        return map



t = Tic([[5, 1, 'x'], [1, 1, 'o'], [1, 3, 'x'], [3, 2, 'o'], [2, 7, 'x'], [7, 4, 'o'], [4, 9, 'x'], [9, 9, 'o'], [9, 6, 'x'], [6, 4, 'o'], [4, 1, 'x'], [1, 9, 'o'], [9, 4, 'x'], [4, 7, 'o'], [7, 9, 'x'], [9, 3, 'o'], [3, 7, 'x'], [7, 3, 'o'], [3, 3, 'x'], [3, 6, 'o'], [6, 7, 'x'], [7, 8, 'o'], [8, 4, 'x'], [4, 4, 'o'], [4, 5, 'x'], [5, 3, 'o'], [3, 5, 'x'], [5, 4, 'o'], [9, 5, 'x'], [5, 2, 'o'], [2, 1, 'x'], [1, 5, 'o'], [5, 9, 'x'], [8, 9, 'o'], [5, 5, 'x'], [3, 8, 'o'], [8, 6, 'x'], [6, 2, 'o']]
)
p = ""
d = ""
while(t.moves() !=[]):
    p = int(raw_input(t.moves()))
    d = int(raw_input())
    t = t.afterMove([p,d])
    if(t.moves !=[] and len(t.x) < 40):
        print len(t.x)
        print t.moves()
        move = randint(0,len(t.moves())-1)
        print t.x
        print t.b
        print t.moves()[move]
        t = t.afterMove(t.moves()[move])
        print t.x
        print t.b
    elif(t.moves !=[]):
        print t.moves()
        move = bestMoveAndScore(t)["move"]
        print t.moves()
        print move
        t = t.afterMove(move)
        print t.moves()
