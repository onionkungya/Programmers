def solution(price, money, count):
    total = []
    for i in range(1, count+1):
        pri = price * i
        total.append(pri)
        
    if money-sum(total) >= 0:
        return 0
    else : 
        return sum(total)-money

#https://school.programmers.co.kr/learn/courses/30/lessons/82612
#Programmers, Level1, 부족한 금액 계산하기
#인상되는 금액을 배열에 담아 문제를 해결했습니다.
