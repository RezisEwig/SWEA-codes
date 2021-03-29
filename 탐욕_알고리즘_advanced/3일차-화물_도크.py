def my_sort(array) :
    for i in range(len(array)) :
        for j in range(i+1, len(array)) :
            if array[i][1] > array[j][1] :
                array[i], array[j] = array[j], array[i]
                
    return array

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    time_table = [list(map(int, input().split())) for _ in range(N)]
    time_table = my_sort(time_table)
    
    end = time_table[0][1]
    task = 1
    time_table.pop(0)
    
    for i in time_table :
        if end <= i[0] :
            end = i[1]
            task += 1

    print("#{0} {1}".format(test_case, task))
    # ///////////////////////////////////////////////////////////////////////////////////