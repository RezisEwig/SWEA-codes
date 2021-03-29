T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    mod, goal = map(int, input().split())
    #zero = [0 for i in range(12)]
    num = list(range(1,13))
    newlist = []
    counter = 0
    
    for a1 in range(2):
        for a2 in range(2):
            for a3 in range(2):
                for a4 in range(2):
                    for a5 in range(2):
                        for a6 in range(2):
                            for a7 in range(2):
                                for a8 in range(2):
                                    for a9 in range(2):
                                        for a10 in range(2):
                                            for a11 in range(2):
                                                for a12 in range(2):
                                                    newlist.append([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12])

    for i in newlist:
        if sum(i)==mod and sum([x*y for x,y in zip(i,num)]) == goal:
            counter += 1

    print("#{0} {1}".format(test_case, counter))
    # ///////////////////////////////////////////////////////////////////////////////////