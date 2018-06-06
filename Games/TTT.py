import copy

def valid_moves(state):
    if not has_won(state):
        moves = []
        for i in enumerate(state[9]):
            if i[1] != 0:
                for p in enumerate(state[i[0]]):
                    if p[1] == 0:
                        moves.append(copy.deepcopy(state))
                        moves[-1][i[0]][p[0]] = i[1]
                        moves[-1][9] = [0]*9
                        if has_won_square(moves[-1][i[0]]):
                            moves[-1][9] = [3-i[1] if has_won_square(n) else 0 for n in moves[-1][:9]]
                        else:
                            moves[-1][9][p[0]] = 3 - i[1]
        return moves


def has_won_square(mini_state, boolean=True):
    winning_pos = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for i in winning_pos:
        if mini_state[i[0]] == mini_state[i[1]] and mini_state[i[1]] == mini_state[i[2]]:
            if boolean == True:
                return True
            else:
                return mini_state[i[0]]
    if boolean == True:
        return False
    else:
        return 0


def has_won(state):
    meta_state = [0]*9
    for i in enumerate(state[:9]):
        meta_state[i[0]] = has_won_square(i[1], False)
    has_won_square(meta_state)

def gen_state():
    return [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0]]
