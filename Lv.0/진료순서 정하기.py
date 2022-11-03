def solution(emergency):
    answer = []
    cp = emergency.copy()
    emergency.sort(reverse=True)
    for i in cp:
        answer.append(emergency.index(i)+1)
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/120835
#Programmers, Level0, 진료순서 정하기
