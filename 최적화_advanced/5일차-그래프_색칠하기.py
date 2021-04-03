def paint(i) :
    global result
    color_set = set(range(1, M+1))
    for k, v in enumerate(real_map[i]) :
        if v == 1 :
            color_set -= {color_map[k]}
    
    if len(color_set) == 0 :
        result = 0
        return
    
    color_map[i] = min(color_set)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, E, M = map(int, input().split())
    map_info = list(list(map(int, input().split())) for _ in range(E))
    real_map = [[0]*(N+1) for _ in range(N+1)]
    color_map = [0]*(N+1)
    result = 1
    
    for temp in map_info :
        i, j = temp[0], temp[1]
        real_map[i][j], real_map[j][i] = 1, 1
    
    for i in range(1, N+1) :
        paint(i)
    
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////