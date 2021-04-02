def dfs(task, start, sub_sum):
    global result, fuel_map
    if len(task) == 0 :
        sub_sum += fuel_map[start][0]
        if sub_sum < result : 
            result = sub_sum
            return
    if sub_sum > result : return
    
    for k, v in enumerate(task):
        sub_sum += fuel_map[start][v]
        task.pop(k)
        dfs(task, v, sub_sum)
        sub_sum -= fuel_map[start][v]
        task.insert(k, v)
    

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    fuel_map = [list(map(int, input().split())) for _ in range(N)]
    result = float("inf")
    n = [n for n in range(1, N)]
    
    dfs(n, 0, 0)
    
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////