import math

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    T, T_end, k = map(float, input().split())
    cost_pre = 987654321  # 이전 비용
    count = 0

    while T > T_end:          # T_end가 될 때까지 반복

        cost_new = cost_pre - 1      # 비용 계산
        count += 1
        diff = cost_new - cost_pre    # 새로운 비용과 이전 비용의 차이

        if diff < 0 or math.exp(-diff/T) > random(0,1):
            cost_pre = cost_new    # 비용이 감소하거나 확률이 랜덤 값보다 더 크면 비용 갱신
            
        T = T * k                 # k : cooling factor
        
    print("#{0} {1}".format(test_case, count))
    # ///////////////////////////////////////////////////////////////////////////////////