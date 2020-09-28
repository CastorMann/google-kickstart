for T in range(int(input())):
    c = 0
    num = int(input())
    lst = list(map(int, input().split()))
    for i in range(1, num-1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            c += 1
    print("Case #{}: {}".format(T+1, c))