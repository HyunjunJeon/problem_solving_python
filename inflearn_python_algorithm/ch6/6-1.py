import sys


def solve(x: int):
    if x == 0:
        return
    else:
        solve(x // 2)
        print(x % 2, end="")


if __name__ == "__main__":
    sys.stdin = open("../pythonalgorithm_formac/섹션 6/1. 재귀함수란(이진수출력)/in1.txt", "rt")
    n = int(input())
    solve(n)

