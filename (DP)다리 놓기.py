import math

def solution(t):
    testcases = []
    for _ in range(t):
        left,right= map(int,input().split())
        if left == 0:
            print(0)
            continue
        print(math.factorial(right) // (math.factorial(left) * math.factorial(right-left)))
        
    
    
solution(int(input()))