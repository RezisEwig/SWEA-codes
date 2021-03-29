T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    V, E = map(int, input().split())
    conection = list(list(map(int, input().split()))for _ in range(E))
    conection.sort(key = lambda conection : conection[2])
    group = [0]*(V+1)
    count = 0
    weight_sum = 0
    
    for i in conection :
        main = i[0]
        sub = i[1]
        weight = i[2]
        
        if group[main] == 0 and group[sub] == 0 :
            count += 1
            group[main], group[sub] = count, count
            weight_sum += weight
        elif group[main] != 0 and group[sub] == 0 :
            count += 1
            group[sub] = group[main]
            weight_sum += weight
        elif group[main] == 0 and group[sub] != 0 :
            count += 1
            group[main] = group[sub]
            weight_sum += weight
        elif group[main] != group[sub] :
            count += 1
            weight_sum += weight
            key = min(group[main], group[sub])
            target = max(group[main], group[sub])
            for i in range(V+1) :
                if group[i] == target : group[i] = key
        #print(main, sub, weight, weight_sum)
        if count == V : break
            
    print("#{0} {1}".format(test_case, weight_sum))
    # ///////////////////////////////////////////////////////////////////////////////////