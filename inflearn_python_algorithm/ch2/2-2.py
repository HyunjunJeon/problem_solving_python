### K번째 수 ###
import sys

# Input 데이터 입력 - stdin
sys.stdin=open("/pythonalgorithm_formac/섹션 2/2. K번째 수/in1.txt", "rt")

t = int(input())

for tc in range(t):
    n,s,e,k = map(int, input().split())
    data = list(map(int, input().split()))

    # s번째부터 e번째까지
    data = data[s-1:e] 

    # 오름차순 정렬(reverse=False 가 디폴트임)
    data.sort(reverse=False)

    # 그 중 k 번째 수를 찾는 것
    print(f"#{tc+1} {data[k-1]}")