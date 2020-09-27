for T in range(1, int(input())+1):
    N, K = map(int, input().split())
    intervals = []
    for _ in range(N): 
        x1, x2 = map(int, input().split())
        intervals.append([x1, x2])
    res = 0
    intervals.sort()
    current_time = 0
    for interval in intervals:
        current_time = max(current_time, interval[0])
        if current_time >= interval[1]: continue
        else:
            num_bots = (interval[1]-current_time-1)//K+1
            res += num_bots
            current_time += num_bots*K
    print("Case #{}:".format(T), res)
    

    