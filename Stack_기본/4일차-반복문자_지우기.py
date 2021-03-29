T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    str = list(input())
    stack = []
    count = 0
    
    for c in str :
        if len(stack) == 0 : 
            stack.append(c)
            continue
        if stack[-1] == c :
            stack.pop()
            count += 1
        else :
            stack.append(c)
    
    result = len(str) - 2*count
    
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////