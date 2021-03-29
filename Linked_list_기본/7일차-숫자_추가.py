T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m, l = map(int, input().split())
    mylist = list(input().split())
    
    for i in range(m) :
        index, value = map(int, input().split())
        mylist.insert(index, value)
        
    print("#{0} {1}".format(test_case, mylist[l]))
    
    # ///////////////////////////////////////////////////////////////////////////////////