def IsSafe(y,x):
    return 0<=y<N and 0<=x<N

def DFS(y,x):
    global sub_result, result

    if result < sub_result:
        return

    if y == N-1 and x == N-1:
        result = sub_result
        return

    for dir in range(2):
        New_Y = y + dy[dir]
        New_X = x + dx[dir]
        if IsSafe(New_Y, New_X) :           
            sub_result += Data[New_Y][New_X]
            DFS(New_Y, New_X)
            sub_result -= Data[New_Y][New_X]


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]

    visited = []

    #우 하
    dy = [0, 1]
    dx = [1, 0]

    sub_result, result = Data[0][0], 987654321
    DFS(0,0)
    print('#%d %d'%(tc, result))