T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    A = list(input() for i in range(N))
    B = list(input() for i in range(M))
    count = 0
    
    for i in A :
        if i in B : count += 1
            
    print("#{0} {1}".format(test_case, count))
    # ///////////////////////////////////////////////////////////////////////////////////
