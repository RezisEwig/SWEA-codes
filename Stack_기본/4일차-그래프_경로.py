def search(s):
    stack.append(s)
    visited[s]=1
    while stack:
        if s==g:
            return 1
        else:
            for i in node[s]:
                if not visited[i]:
                    visited[i]=1
                    stack.append(i)
            s=stack.pop()
    return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    v,e=map(int,input().split())
    visited=[0]*(v+1)
    node=[[] for _ in range(v+1)]
    stack=[]
    for _ in range(e):
        start,end=map(int,input().split())
        node[start].append(end)
    s,g=map(int,input().split())
    result = search(s)
    
    print("#{} {}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////