SELECT NAME, COUNT(NAME) AS 'COUNT'
FROM ANIMAL_INS
GROUP BY NAME HAVING COUNT(NAME)>=2
ORDER BY NAME;

#https://school.programmers.co.kr/learn/courses/30/lessons/59041
#Programmers, Lv2, 동명 동물 수 찾기
#GROUP BY 절의 HAVING 조건을 이용하여 문제를 해결하였습니다.
