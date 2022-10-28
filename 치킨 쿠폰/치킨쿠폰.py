def solution(chicken):
    answer = 0
    while chicken >=10 :
        service = chicken//10
        remainder = chicken%10
        answer += service
        chicken = service + remainder
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/120884
#Programmers, Level0, 치킨 쿠폰
#while 문을 사용하여 문제를 해결했습니다.
