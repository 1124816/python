#game.moves()
#game.afterMove(move)
#game.score()

def bestMoveAndScore(game):
    score = -2
    best_move
    for move in game.moves():
        move_score = score(game, move)
        if move_score > score:
            score = move_score
            best_move = move
    return {"move":best_move ,"score":score}

def score(game, move):
    game = game.afterMove(move)
    if game.moves() == []:
        return game.score()
    else:
        return -bestMoveAndScore["score"]
