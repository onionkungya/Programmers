def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/12951
#Programmers. Lv2, JadenCase 문자열 만들기
#' '(Spacebar)를 기준으로 문자열을 리스트로 바꾸고 captalize 내장함수를 사용해 첫글자만 대문자로 만들어 문제를 해결하였습니다.
