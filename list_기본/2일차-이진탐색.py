T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    page , pA , pB = map(int, input().split())
    startA, endA = 1, page
    startB, endB = 1, page
    phaseA, phaseB = 1, 1
    
    while startA < endA:
        c = startA + (endA - startA) // 2
        if c == pA: break
        elif c > pA : endA = c
        else : startA = c
        phaseA += 1

    while startB < endB:
        c = startB + (endB - startB) // 2
        if c == pB: break
        elif c > pB : endB = c
        else : startB = c
        phaseB += 1
        
    if phaseA < phaseB : result = "A"
    elif phaseA > phaseB : result = "B"
    else : result = 0
        
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////