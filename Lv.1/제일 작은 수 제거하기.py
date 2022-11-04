def solution(arr):
    answer = []
    arr.remove(min(arr))
    if len(arr) < 1 :
        arr.append(-1)
    return arr

#https://school.programmers.co.kr/learn/courses/30/lessons/12935
#Programmers, Lv1, 제일 작은 수 제거하기
