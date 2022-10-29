def solution(numbers):
    answer = 0
    whole = [0, 1, 2, 3, 4, 5, 6, 7, 8,9]
    for i in range(len(numbers)):
        whole.remove(numbers[i])
    for i in range(len(whole)):
        answer += whole[i]
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/86051
#Programmers, Level1, 없는 숫자 더하기
#1~9까지의 배열을 새로 만들고 numbers의 값을 빼주는 방식으로 문제를 해결했습니다.
