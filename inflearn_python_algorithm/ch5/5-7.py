import sys
from collections import deque


def solve(check: str, input: str):
    check = deque(check)
    for x in input:
        if x in check:
            if x != check.popleft():
                return "NO"
    else:
        if len(check) == 0:
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/7. 교육과정 설계/in1.txt", "rt")
    check = input()
    N = int(input())
    for i in range(N):
        print(f"#{i} ", solve(check, input()))