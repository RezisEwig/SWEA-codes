T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m = map(int, input().split())
    queue = list(input().split())
    
    for i in range(m) :
        t = queue.pop(0)
        queue.append(t)
    print("#{0} {1}".format(test_case, queue.pop(0)))
    # ///////////////////////////////////////////////////////////////////////////////////