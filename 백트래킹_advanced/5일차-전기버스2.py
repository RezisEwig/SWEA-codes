def simulation(station, goal, position, change, power) :
    global best
    #print(position, change, power)
    if change >= best : return
    if position >= goal : 
        best = change
        return
    
    if power == 0 :
        change += 1
        #print(position, change, power)
        power = station[position-1]
        simulation(station, goal, position+1, change, power-1)
    else :
        simulation(station, goal, position+1, change, power-1)
        change += 1
        power = station[position-1]
        simulation(station, goal, position+1, change, power-1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    station = list(map(int, input().split()))
    goal = station.pop(0)
    best = 987654321
    
    simulation(station, goal, 1, -1, 0)
    
    print("#{0} {1}".format(test_case, best))
    # ///////////////////////////////////////////////////////////////////////////////////