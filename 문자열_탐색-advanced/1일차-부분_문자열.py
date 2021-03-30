T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, sentence = map(str, input().split())
    N = int(N)
    storage = set()
    
    for s in range(len(sentence)) :
        for end in range(s, len(sentence)) :
            storage.add(sentence[s:end+1])
            
    storage = sorted(list(storage))
    
    print("#{0} {1} {2}".format(test_case, storage[N-1][0], len(storage[N-1])))
    # ///////////////////////////////////////////////////////////////////////////////////
