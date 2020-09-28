def conv(R, P): return (R-1)**2+P-1
def replace(ind, lst): 
    new = lst.copy()
    new[ind] = 0
    return new

def minimax(museum, p1, p2, turn, score):
    n1 = [i for i in neighbours[p1] if museum[i]]
    n2 = [i for i in neighbours[p2] if museum[i]]
    if not n1+n2: return score
    if turn:
        if not n1: return minimax(museum, p1, p2, not turn, score)
        return max([minimax(replace(ind, museum), ind, p2, False, score+1) for ind in n1])
    else:
        if not n2: return minimax(museum, p1, p2, not turn, score)
        return min([minimax(replace(ind, museum), p1, ind, True, score-1) for ind in n2])


for T in range(1, int(input())+1):
    S, Ra, Pa, Rb, Pb, C = map(int, input().split())
    under_construction = [tuple(map(int, input().split())) for _ in range(C)]
    player_one_position = conv(Ra, Pa)
    player_two_position = conv(Rb, Pb)
    museum = [1 for i in range(S**2)]
    museum[player_one_position], museum[player_two_position] = 0, 0
    for R, P in under_construction: museum[conv(R, P)] = 0

    neighbours = dict()
    for R in range(1, S+1):
        for P in range(1, 2*R):
            lst = []
            if R % 2 == 0:
                if P % 2 == 0:
                    lst.append(conv(R-1, P-1))
                elif R != S:
                    lst.append(conv(R+1, P+1))
            else:
                if P % 2 == 0:
                    lst.append(conv(R-1, P-1))
                elif R != S:
                    lst.append(conv(R+1, P+1))
            if P > 1: lst.append(conv(R, P-1))
            if P < 2 * R - 1: lst.append(conv(R, P+1))
            neighbours[conv(R, P)] = lst
    
    res = minimax(museum, player_one_position, player_two_position, True, 0)
    print("Case #{}:".format(T), res)
    


        



