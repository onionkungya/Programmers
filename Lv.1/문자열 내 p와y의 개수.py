def solution(s):
    answer = True
    p = 0
    y = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i]=='P' :
            p += 1
        elif s[i]=='y' or s[i]=='Y' :
            y += 1
    if p==y :
        return True
    else :
        return False

#https://school.programmers.co.kr/learn/courses/30/lessons/12916
#Programmers, Lv1, 문자열 내 p와y의 개수
