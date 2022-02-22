import sys
from collections import deque


def solve(N:int, M:int, data: list):
    patient = deque()
    [patient.append((idx, d)) for idx, d in enumerate(data)]
    cnt = 0
    while True:
        cur = patient.popleft()
        if any(cur[1] < x[1] for x in patient):
            patient.append(cur)
        else:
            cnt += 1
            if cur[0] == M:
                break
    return cnt


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/6. 응급실/in1.txt", "rt")
    N, M = map(int, input().split())
    dangerous = list(map(int, input().split()))
    print(solve(N, M, dangerous))