T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    mylist = list(map(int, input().split()))
    N = len(mylist)
    long_list = [1]*N
    
    for i in range(N):
        for j in range(i):
            if mylist[i] > mylist[j] :
                long_list[i] = max(long_list[i], long_list[j] + 1)
                
    print("#{0} {1}".format(test_case, max(long_list)))
    # ///////////////////////////////////////////////////////////////////////////////////