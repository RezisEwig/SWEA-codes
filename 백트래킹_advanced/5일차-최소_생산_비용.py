def contract(money_table, visited, sub_total, depth, k) :
    global best
    #print(sub_total)
    if sub_total >= best : return
    if depth == k :
        best = sub_total
        return
    
    for i in range(1,N+1) :
        if visited[i] == 0 :
            visited[i] = 1
            sub_total += money_table[depth][i-1]
            contract(money_table, visited, sub_total, depth+1, k)
            visited[i] = 0
            sub_total -= money_table[depth][i-1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    money_table = []
    for i in range(N) :
        money_table.append(list(map(int, input().split())))
    visited = [0 for _ in range(N+1)]
    best = 987654321
    
    contract(money_table, visited, 0, 0, N)
    
    print("#{0} {1}".format(test_case, best))
    # ///////////////////////////////////////////////////////////////////////////////////