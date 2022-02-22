import sys

# Input 데이터 입력 - stdin
sys.stdin=open("/pythonalgorithm_formac/섹션 2/3. k번째 큰 수/in1.txt", "rt")

n,k = map(int, input().split())
data = list(map(int, input().split()))
res = set() # 중복을 방지하기 위해

# 데이터에서 3개를 뽑아서 합한 수의 리스트(i,j,m) 
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(data[i] + data[j] + data[m])

result = list(res)
result.sort(reverse=True) # 내림차순으로 정렬해서 k번쨰 큰 수를 추출해야함

# 그 중 k번째로 큰 값
print(result[k-1])