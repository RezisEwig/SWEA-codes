T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    str = list(input())
    stack = []
    result = 1

    for s in str:
        if s == '{' or s == '(' : stack.append(s)
        if s == '}' or s == ')' : 
            try :
                v = stack.pop()
                if s == '}' and v != '{' :
                    result = 0
                    break
                if s == ')' and v != '(' :
                    result = 0
                    break
            except:
                result = 0
    
    try :
        stack.pop()
        result = 0
    except:
        result = result
        
    print("#{0} {1}".format(test_case, result))
    # ///////////////////////////////////////////////////////////////////////////////////