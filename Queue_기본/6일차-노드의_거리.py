T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    v, e = map(int, input().split())
    visited = [0 for _ in range(v+1)]
    distance = [0 for _ in range(v+1)]
    way = [[] for x in range(v+1)]
    queue = []
    phase = 0
    
    for i in range(e) :
        temp = list(map(int, input().split()))
        way[temp[0]].append(temp[1])
        way[temp[1]].append(temp[0])
    
    start, end = map(int, input().split())
    
    queue.append(start)
    visited[start] = 1
    while(len(queue)) :
        phase += 1
        for _ in range(len(queue)) :
            for i in way[queue.pop(0)] :
                if visited[i] == 0 :
                    visited[i] = 1
                    queue.append(i)
                    distance[i] = phase
                    #print(distance)
                if i == end :
                    queue = []
                    break
            if len(queue) == 0 :
                break
    
    print("#{0} {1}".format(test_case, distance[end]))
    # ///////////////////////////////////////////////////////////////////////////////////