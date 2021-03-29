T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m = map(int, input().split())
    mylist = list(map(int, input().split()))
    
    for i in range(m-1) :
        temp = list(map(int, input().split()))
        #print(temp)
        for j in range(len(mylist)) :
            if mylist[j] > temp[0] :
                mylist[j:j] = temp
                #print(mylist)
                #for k, p in enumerate(temp) :
                    #mylist.insert(j+k, p)
                    #print(mylist)
                break
            if j == len(mylist)-1 :
                mylist.extend(temp)
                #print(mylist)
    #print(mylist)
    result = mylist[-1:-11:-1]
    #print(result)
    print("#{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}".format(test_case, result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]))
            
    # ///////////////////////////////////////////////////////////////////////////////////
