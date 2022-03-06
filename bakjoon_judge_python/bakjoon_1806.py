# https://www.acmicpc.net/problem/1806
# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
# 이 수열에서 **연속된 수들의 부분합** 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이
import sys

n, s = map(int, input().split())
data = list(map(int, input().split()))

min_length = sys.maxsize
temp_sum = 0
start, end = 0, 0

while True:
    if temp_sum >= s:
        # 합이 S 이상이 되면, 사이즈를 저장하고 + start 포인터를 한칸 전진시켜 부분합 사이즈를 축소해봄
        min_length = min(min_length, end - start)
        temp_sum -= data[start]
        start += 1

    elif end == n:
        # end 포인터가 배열 끝에 다다르면 종료함(더이상 부분합을 구할 수 없으므로)
        break

    else:
        # end 포인터를 한칸씩 전진시키며 연속된 부분합 사이즈를 늘려나감
        temp_sum += data[end]
        end += 1

print(min_length) if min_length == sys.maxsize else print(0)