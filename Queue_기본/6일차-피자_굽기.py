T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m = map(int, input().split())
    queue = []
    pizza = list(map(int, input().split()))
    
    for i, k in enumerate(pizza) :
        pizza[i] = [i+1, k]

    while(True) :
        if len(pizza) > 0 and len(queue) < n :
            queue.append(pizza.pop(0))
            continue
        out = queue.pop(0)
        out[1] = out[1]//2
        
        if out[1] != 0 :
            queue.append(out)
        
        if len(queue) == 0 :
            break
        
    print("#{0} {1}".format(test_case, out[0]))
    # ///////////////////////////////////////////////////////////////////////////////////
