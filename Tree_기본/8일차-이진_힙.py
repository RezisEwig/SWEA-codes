def bi_sort(tree) :
    index = len(tree)-1
    while (tree[index] < tree[index//2]) :
        tree[index], tree[index//2] = tree[index//2], tree[index]
        index = index // 2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    bi_tree = [0]
    queue = list(map(int, input().split()))
    result = 0
    
    for num in queue :
        bi_tree.append(num)
        bi_sort(bi_tree)
        
    index = N
    while (index//2 != 0) :
        index = index//2
        result += bi_tree[index]
                
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////