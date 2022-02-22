import sys


# 가장 일반적으로 문제의 답만을 고려한 풀이
def solve(data: list, M: int):
    data.sort()
    return data.index(M) + 1


# 이분검색 스터디를 위한 코드
def solve_이분검색(data: list, N:int, M: int):
    data.sort() # 정렬이 되어 있는 상태에서~
    lt = 0
    rt = N - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if data[mid] == M:
            return mid + 1
        elif data[mid] > M:
            rt = mid - 1
        else:
            lt = mid + 1


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/1. 이분검색/in1.txt", "rt")
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    print(solve(data, M))
    print(solve_이분검색(data, N, M))