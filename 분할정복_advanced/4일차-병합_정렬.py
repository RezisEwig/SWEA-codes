def divine_sort(array) :
    global count
    new_list = []
    N = len(array)
    
    if N == 1 :
        return array
    
    left = divine_sort(array[0:N//2])
    right = divine_sort(array[N//2:N])
    
    flag = False

    for i in range(len(left) + len(right)) :
        if len(left) == 0 :
            new_list.append(right.pop(0))
            continue
        if len(right) == 0 :
            new_list.append(left.pop(0))
            flag = True
            continue
        if left[0] > right[0] : new_list.append(right.pop(0))
        else : new_list.append(left.pop(0))
            
    if flag == True : count += 1
    return new_list
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    my_list = list(map(int, input().split()))
    count = 0
    
    my_list = divine_sort(my_list)
    
    print("#{0} {1} {2}".format(test_case, my_list[len(my_list)//2], count))
    # ///////////////////////////////////////////////////////////////////////////////////