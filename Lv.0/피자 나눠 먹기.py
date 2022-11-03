#피자 나눠 먹기 (1)
def solution(n):
    import math
    return math.ceil(n/7)


#피자 나눠 먹기 (2)
def solution(n):
    for i in range(1, n+1) :
        if (i*6)%n == 0 :
            return i


#피자 나눠 먹기 (3)
def solution(slice, n):
    import math
    return math.ceil(n/slice)

#https://school.programmers.co.kr/learn/courses/30/lessons/120814
#https://school.programmers.co.kr/learn/courses/30/lessons/120815
#https://school.programmers.co.kr/learn/courses/30/lessons/120816
#Programmers, Level0, 피자 나눠 먹기
