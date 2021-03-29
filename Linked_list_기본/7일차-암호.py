T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m, k = map(int, input().split())
    mylist = list(map(int, input().split()))
    head = 0
    for i in range(k) :
        #print(mylist)
        if head+m >= n and (head+m)%n == 0 :
            head = -1
            n = n+1
            mylist.append(mylist[0] + mylist[-1])
        else :
            head = (head+m)%n
            n = n+1
            #print(head)
            mylist.insert(head, mylist[head-1] + mylist[head])

    print("#{}".format(test_case), *mylist[-1:-11:-1])
    #print("".join(x for x in *mylist[-1:-11:-1]))
            
    # ///////////////////////////////////////////////////////////////////////////////////
