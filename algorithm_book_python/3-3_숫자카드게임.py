n, m = map(int, input().split())
data = list()
[data.append(min(list(map(int, input().split())))) for _ in range(n)] # 애초에 최소값을 넣어줌

# 각 행에 포함된 카드들 중 가장 작은 수를 찾은 뒤 그 수 중 가장 큰 수
print(max(data))
