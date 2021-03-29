T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    array = list(map(int, input().split()))
    for i in range(10):
        val, index = array[i], i
        if i%2 == 0:
            for j in range(i+1, n):
                if array[j] > val : val, index = array[j], j
        else:
            for j in range(i+1, n):
                if array[j] < val : val, index = array[j], j

        array[i], array[index] = array[index], array[i]
        
    print("#{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}".format(test_case, array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9]))
    # ///////////////////////////////////////////////////////////////////////////////////