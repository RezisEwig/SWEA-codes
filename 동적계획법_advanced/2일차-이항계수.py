T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, a, b = map(int, input().split())
    index = min(a,b)
    mylist = [[1] for _ in range(n+1)]
    
    for i in range(n+1) :
        for j in range(1, i+1):
            if i == j : mylist[i].append(1)
            else : mylist[i].append(mylist[i-1][j-1] + mylist[i-1][j])
                
    print("#{0} {1}".format(test_case, mylist[n][index]))
    # ///////////////////////////////////////////////////////////////////////////////////