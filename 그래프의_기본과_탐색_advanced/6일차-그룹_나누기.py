T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    mylist = list(map(int, input().split()))
    student = [0]*(N+1)
    count = 0
    group = 1
    for i in range(0, M*2, 2) :
        main = mylist[i+1]
        sub = mylist[i]

        if student[main] == 0 and student[sub] == 0 : 
            count += 1
            student[main], student[sub] = group, group 
            group += 1
        elif student[main] != 0 and student[sub] == 0 :
            student[sub] = student[main]
        elif student[main] == 0 and student[sub] != 0 :
            student[main] = student[sub]
        elif student[main] != 0 and student[sub] != 0 : 
            if student[main] != student[sub] :
                count -= 1
                key = student[sub]
                for j in range(len(student)) :
                    if student[j] == key :
                        student[j] = student[main]
        
    for i in student :
        if i == 0 :
            count += 1
    
    print("#{0} {1}".format(test_case, count-1))
    # ///////////////////////////////////////////////////////////////////////////////////