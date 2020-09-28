import requests
for T in range(int(input())):
    string = input().strip()
    w = 0
    h = 0
    m = 1
    x = []
    for i in range(len(string)):
        if string[i] == "N": h-=m
        elif string[i] == "S": h+=m
        elif string[i] == "W": w-=m
        elif string[i] == "E": w+=m
        elif string[i] == "(": continue
        elif string[i] == ")":
            m/=x.pop()
        else:
            m*=int(string[i])
            x.append(int(string[i]))
        w %= 1000000000
        h %= 1000000000
    w, h = int(w), int(h)
    print("Case #{}: {} {}".format(T+1, w+1, h+1))