for T in range(int(input())):
    info = list(map(int, input().split()))
    times = list(map(int, input().split()))
    D = info[1]
    while times:
        D -= D%times.pop()
    print("Case #{}: {}".format(T+1, D))