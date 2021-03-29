T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())
    field = [[0 for i in range(10)] for j in range(10)] 
    counter = 0

    for _ in range(n):
        color = list(map(int, input().split()))
        if color[4] == 1 :
            for i in range(color[0], color[2]+1):
                for j in range(color[1], color[3]+1):
                    if field[i][j] == 0 : field[i][j] = 1
                    elif field[i][j] == 2 : field[i][j] = 3
        else:
            for i in range(color[0], color[2]+1):
                for j in range(color[1], color[3]+1):
                    if field[i][j] == 0 : field[i][j] = 2
                    elif field[i][j] == 1 : field[i][j] = 3
    
    for i in range(10):
        for j in range(10):
            if field[i][j] == 3 : counter += 1
                
    print("#{0} {1}".format(test_case, counter))