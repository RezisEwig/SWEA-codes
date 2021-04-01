T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    price = list(list(map(int, input().split())) for _ in range(M))
    mylist = [[0]*(N+1) for _ in range(M+1)]
    
    for depth in range(M+1) :
        for w in range(N+1) :
            if depth == 0 or w == 0 : continue
            if w < price[depth-1][0] : mylist[depth][w] = mylist[depth-1][w]
            else : mylist[depth][w] = max(mylist[depth-1][w-price[depth-1][0]] + price[depth-1][1], mylist[depth-1][w])
                
    print("#{0} {1}".format(test_case, mylist[M][N]))