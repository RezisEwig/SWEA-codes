T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m, l = map(int, input().split())
    mylist = list(map(int, input().split()))
    
    for i in range(m) :
        work = list(input().split())
        if work[0] == 'I' :
            mylist.insert(int(work[1]), int(work[2]))
        elif work[0] == 'C' :
            mylist[int(work[1])] = int(work[2])
        elif work[0] == 'D' :
            mylist.pop(int(work[1]))
            
    if l > len(mylist) : result = -1
    else : result = mylist[l]
    
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////