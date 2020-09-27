for T in range(1, int(input())+1):

    N, X = map(int, input().split())                        # read lenght of Queue, N, and max amount, X

    lst = input().split()                                   # read list of amounts per person

    lst = map(lambda x: (int(x)-1)//X, lst)                 # convert list to list of number of times the person has to go back         

    lst = list(enumerate(lst))                              # enumerate list

    lst = sorted(lst, key = lambda x: x[1])                 # sort list based on number of 'go backs'

    lst = list(map(lambda x: x[0]+1, lst))                  # strip list

    print("Case #{}:".format(T), " ".join(map(str, lst)))   # print result

