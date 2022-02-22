### K번째 약수 ###
import sys

# 입력 받아서 변수에 할당
sys.stdin=open("/pythonalgorithm_formac/섹션 2/1. k번째 약수/in2.txt", "rt")
n, k=map(int, input().split())

# 약수 구하는 로직
cnt = 0 # 약수 몇번째인지 카운트

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break   # for-else 구문: for문과 같은 레벨에 else를 둬서 break없이 빠져나온 경우를 처리함
else:                       
    print(-1)
