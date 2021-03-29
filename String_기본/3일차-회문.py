T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    storage = []
    answer = []
    for i in range(N):
        storage.append(input())

    for s in storage:
        for i in range(N-M+1):
            for k in range(M//2):
                if s[i+k] != s[i+M-k-1] : break
                if k == (M//2-1) : answer = s[i:i+M]
                    
    storage = ["".join(x) for x in zip(*storage)]
    
    for s in storage:
        for i in range(N-M+1):
            for k in range(M//2):
                if s[i+k] != s[i+M-k-1] : break
                if k == (M//2-1) : answer = s[i:i+M]
                    
    print("#{0} {1}".format(test_case, answer))
    # ///////////////////////////////////////////////////////////////////////////////////