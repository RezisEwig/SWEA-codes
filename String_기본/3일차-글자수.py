T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    str1 = input()
    str2 = input()
    combo, result = 0, 0
    
    for i in range(len(str1)):
        combo = 0
        for j in range(len(str2)):
            if str1[i] == str2[j] : combo += 1
        if result < combo : result = combo
            
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////