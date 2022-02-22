import sys

sys.stdin = open("/pythonalgorithm_formac/섹션 2/5. 정다면체/in1.txt", "rt")

N,M = map(int, input().split()) # 4,6,8,12,20 중 하나임

cnt = [0] * (N + M + 2)
max_n = -1

for n in range(1, N+1):
    for m in range(1, M+1):
        cnt[n+m] += 1

for i in range(N+M+1):
    if cnt[i] > max_n:
        max_n = cnt[i]

for i in range(N+M+1):
    if cnt[i] == max_n:
        print(i, end=" ")