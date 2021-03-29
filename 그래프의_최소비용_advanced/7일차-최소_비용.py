def isSafe(x, y) :
    return -1 < x < N and -1 < y < N


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    height_map = list(list(map(int, input().split())) for _ in range(N))
    fuel_map = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    queue = [(0,0)]
    fuel_map[0][0] = 0
    visited[0][0] = 1
    
    while queue :
        #print(queue, fuel_map, visited)
        position = queue.pop(0)
        x = position[0]
        y = position[1]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        for i in range(4) :
            newX = x+dx[i]
            newY = y+dy[i]
            if isSafe(newX, newY) :
                height_gap = height_map[newX][newY] - height_map[x][y]
                if height_gap < 0 : height_gap = 0
                    
                if visited[newX][newY] == 0 :
                    visited[newX][newY] = 1
                    fuel_map[newX][newY] = fuel_map[x][y] + height_gap + 1
                    queue.append((newX, newY))
                elif (fuel_map[x][y] + height_gap + 1) < fuel_map[newX][newY] :
                    fuel_map[newX][newY] = fuel_map[x][y] + height_gap + 1
                    queue.append((newX, newY))

    print("#{0} {1}".format(test_case, fuel_map[N-1][N-1]))
    # ///////////////////////////////////////////////////////////////////////////////////
