T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, E = map(int, input().split())
    way_map = list(list(map(int, input().split())) for _ in range(E))
    way_map.sort(key = lambda way_map : way_map[0])
    distance_map = [0]*(N+1)
    visited = [0]*(N+1)
    visited[0] = 1
    queue = [0]
    
    while queue :
        position = queue.pop(0)
        for i in way_map :
            start = i[0]
            end = i[1]
            distance = i[2]
            if start == position :
                if visited[end] == 0 :
                    visited[end] = 1
                    distance_map[end] = distance_map[start] + distance
                    queue.append(end)
                elif distance_map[end] > distance_map[start] + distance :
                    distance_map[end] = distance_map[start] + distance
                    queue.append(end)
                    
    print("#{0} {1}".format(test_case, distance_map[N]))
    # ///////////////////////////////////////////////////////////////////////////////////
