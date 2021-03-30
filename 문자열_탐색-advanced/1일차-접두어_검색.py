T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    A = list(input() for _ in range(N))
    B = list(input() for _ in range(M))
    count = 0
    
    for b in B:
        flag = 0
        for a in A:
            if flag == 1 : break 
            for i in range(len(b)):
                if i+1 > len(a) or a[i] != b[i] : break
                if i+1 == len(b) : 
                    count += 1
                    flag = 1
                    
    print("#{0} {1}".format(test_case, count))
    # ///////////////////////////////////////////////////////////////////////////////////