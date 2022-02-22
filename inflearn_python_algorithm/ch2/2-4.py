import sys

## 최소값 구하기 연습
arr = [5,3,7,9,2,5,2,6]
arrMin = float('inf') # infinite 의 약자

for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]

# print(arrMin)

# Input 데이터 입력 - stdin
sys.stdin=open("/pythonalgorithm_formac/섹션 2/4. 대표값/in1.txt", "rt")

N = int(input())
scores = list(map(int, input().split()))

avg = int(round(sum(scores) / N))

minimum = sys.maxsize

for idx, i in enumerate(scores):
    tmp = abs(i-avg)
    if tmp < minimum:
        minimum = tmp
        score = i
        res = idx + 1
    elif tmp == min:
        if i > score:
            score = i
            res = idx + 1

print(f"{avg} {res}")
