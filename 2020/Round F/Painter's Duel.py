for T in range(1, int(input())+1):
    S, Ra, Pa, Rb, Pb, C = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(C)]
    visited = []