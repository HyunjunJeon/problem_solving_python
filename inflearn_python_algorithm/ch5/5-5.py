import sys
from collections import deque


def solve(N: int, K: int):
    prince = deque(list(range(1, N+1)))
    while prince:
        for _ in range(K-1):
            prince.append(prince.popleft())  # 앞에서 빼서 뒤로 넣어줌
        if len(prince) == 1:
            return prince.pop()
        else:
            prince.popleft()


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/5. 공주구하기/in2.txt", "rt")
    N, K = map(int, input().split())
    print(solve(N, K))