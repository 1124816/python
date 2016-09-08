#game.moves()
#game.afterMove(move)
#game.score()

import math

tocan = 0

def scorer(game, bMove):
    game = game.afterMove(bMove)
    if game.moves() == []:
        return game.score()
    else:
        return -bestMoveAndScore(game)["score"]

def bestMoveAndScore(game):
    global tocan
    score = -2
    best_move = False
    for move in game.moves():
        tocan = tocan + 1
        print tocan
        move_score = scorer(game, move)
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
        if(out!=-1):
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
            if(p[0]==1|p[0]==5|p[0]==9):
                w[6].append(p[1])
            elif(p[0]==3|p[0]==5|p[0]==7):
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
                    if(p[1]==1|p[1]==5|p[1]==9):
                        w[6].append(p[2])
                    elif(p[1]==3|p[1]==5|p[1]==7):
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



t = Tic()
p = ""
d = ""
while(t.moves() !=[]):
    p = int(raw_input(t.moves()))
    d = int(raw_input())
    t = t.afterMove([p,d])
    if(t.moves !=[]):
        print t.moves()
        move = bestMoveAndScore(t)["move"]
        print t.moves()
        print move
        t = t.afterMove(move)
        print t.moves()
