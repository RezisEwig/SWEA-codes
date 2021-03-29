from itertools import permutations

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    fuel_map = [list(map(int, input().split())) for _ in range(N)]
    way = list(permutations(range(2, N+1)))
    result, sub_result = 987654321, 0
    
    for i in way :
        start = 1
        sub_result = 0
        for k in i :
            end = k
            sub_result += fuel_map[start-1][end-1]
            if sub_result > result : 
                sub_result = 987654321
                break
            start = end
        sub_result += fuel_map[end-1][0]
        if result > sub_result : result = sub_result
    
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////