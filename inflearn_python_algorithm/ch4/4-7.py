import sys


def my_solve(L:int, data: list, M: int):
    for _ in range(M):
        data.sort()
        data[L-1] -= 1
        data[0] += 1

    return max(data) - min(data)


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/7. 창고 정리/in5.txt", "rt")
    L = int(input())
    data = list(map(int, input().split()))
    M = int(input())
    print(my_solve(L, data, M))