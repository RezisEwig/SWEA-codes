T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    mymap = [[0]*2 for _ in range(E+2)]
    queue = []
    index, value = 0, 1
    count = 0
    
    for i in range(len(temp)//2) :
        if mymap[temp[index]][0] == 0 :
            mymap[temp[index]][0] = temp[value]
        else :
            mymap[temp[index]][1] = temp[value]
        index += 2
        value += 2
    #print(mymap)
    queue.append(N)
    
    while(len(queue)) :
        temp = queue.pop(0)
        count += 1
        for i in range(2) :
            if mymap[temp][i] != 0 :
                queue.append(mymap[temp][i])
                
    print("#{0} {1}".format(test_case, count))
    # ///////////////////////////////////////////////////////////////////////////////////