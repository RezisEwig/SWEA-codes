T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num = float(input())
    bi_num = ""
    divide = 1
    
    for i in range(12) :
        divide = divide/2
        if num >= divide : 
            bi_num = bi_num + '1'
            num -= divide
        else : bi_num = bi_num + '0'
        if num == 0.0 : break
        #print(num, bi_num)
    
    if num > 0.0 : bi_num = 'overflow'
    
    print("#{0} {1}".format(test_case, bi_num))
    # ///////////////////////////////////////////////////////////////////////////////////
