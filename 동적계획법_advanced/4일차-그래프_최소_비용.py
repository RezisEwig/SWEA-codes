T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    distance = list(list(map(int, input().split())) for _ in range(N))
    max_val = 0
    
    for i in range(N):
        for j in range(N):
            if distance[i][j] == 0 : distance[i][j] = float("inf")
                
    for k in range(N):
        for i in range(N):
            if k == i : continue
            for j in range(N):
                if k == j or j == i : continue
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    for i in range(N):
        for j in range(N):
            if distance[i][j] != float("inf") and distance[i][j] > max_val : max_val = distance[i][j]
                
    print("#{0} {1}".format(test_case, max_val))
                           
    # ///////////////////////////////////////////////////////////////////////////////////