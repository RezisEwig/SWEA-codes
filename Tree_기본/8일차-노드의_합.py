def bi_sum(index) :
    global bi_tree
    global N
    if index*2 <= N :
        bi_sum(index*2)
        bi_tree[index] += bi_tree[index*2]
    if index*2+1 <= N :
        bi_sum(index*2+1) 
        bi_tree[index] += bi_tree[index*2+1]
    

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, L = map(int, input().split())
    bi_tree = [0 for _ in range(N+1)]
    for i in range(M) :
        index, value = map(int, input().split())
        bi_tree[index] = value
    
    bi_sum(1)
        
    print("#{0} {1}".format(test_case, bi_tree[L]))
    # ///////////////////////////////////////////////////////////////////////////////////