T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    total_weight = 0
    
    containers.sort(reverse = True)
    trucks.sort(reverse = True)
    
    for t in trucks :
        for i, c in enumerate(containers) :
            if t >= c :
                total_weight += c
                containers.pop(i)
                break
    
    print("#{0} {1}".format(test_case, total_weight))    
    # ///////////////////////////////////////////////////////////////////////////////////
