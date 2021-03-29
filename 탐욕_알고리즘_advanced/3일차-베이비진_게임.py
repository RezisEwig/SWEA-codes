def isBabyGin(array) :
    container = [0 for _ in range(10)]
    for i in array :
        container[i] += 1
        
    for i in range(10) :
        if container[i] >= 3 : return True
        
    for i in range(8) :
        if container[i] > 0 and container[i+1] > 0 and container[i+2] > 0 : return True
        
    return False


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    deck = list(map(int, input().split()))
    p1, p2 = [], []
    result = 0
    p1.append(deck[0])
    p2.append(deck[1])
    p1.append(deck[2])
    p2.append(deck[3])
    
    for i in range(4, 12, 2) :
        p1.append(deck[i])
        if isBabyGin(p1) :
            result = 1
            break
        p2.append(deck[i+1])
        if isBabyGin(p2) :
            result = 2
            break
            
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////