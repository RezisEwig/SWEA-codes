def dfs(R, K):
    global count
    if K == 0 : 
            count += 1
            return
    if K < 0 or sum(R) < K : return
 
    dfs(R[:-1], K-R[-1])
    dfs(R[:-1], K)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    R = list(range(1,N+1))
    count = 0
    
    dfs(R, K)
    print("#{0} {1}".format(test_case, count))
    # ///////////////////////////////////////////////////////////////////////////////////