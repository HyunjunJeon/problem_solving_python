import sys
from collections import deque

def solve(N: int, M: int, data: list):
    # 2명 이하, M kg 제한
    # 승객 모두가 탈출하기 위한 구명보트의 최소 개수

    d_data = deque(data)  # 효율적인 연산을 위해서 deque를 씀
    data.sort()
    cnt = 0
    # 맨 앞, 맨 뒤 꺼내서 더함
    # M보다 작거나 같은지 체크.
    # 작거나 같으면 +1 하고 없앰
    # 크면 걔만 보트 태워버림
    while data:
        if len(data) == 1:
            cnt += 1
            break

        if data[0] + data[-1] > M:
            data.pop()
            cnt += 1
        else:
            data.pop(0)  # 굉장히 비효율적인 연산임(맨 앞에껄 빼면 다 뒤에서 하나씩 땡겨야함)
            d_data.popleft()  # deque 를 이용해 효율적인 연산 수행
            data.pop()
            cnt += 1

    return cnt




if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/8. 침몰하는 타이타닉/in5.txt", "rt")
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    print(solve(N, M, data))