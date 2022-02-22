# 에라토스테네스 체
import sys

# 입력 받아서 변수에 할당
sys.stdin=open("/pythonalgorithm_formac/섹션 2/7. 소수(에라토스테네스 체)/in1.txt", "rt")

N = int(input())

che = [0] * (N+1)
cnt = 0

for i in range(2, N+1):
    if che[i] == 0:
        cnt += 1
        for j in range(i, N+1, i): # i의 배수로 돌게끔
            che[j] = 1

print(cnt)