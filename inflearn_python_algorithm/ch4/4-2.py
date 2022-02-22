import sys


def solve(N: int, data: list):
    # 나올 수 있는 경우의 수는 1 ~ 제일 큰 수
    lt = 1
    rt = max(data)
    results = list()
    while lt <= rt:
        result = 0
        mid = (lt + rt) // 2
        for i in data:
            result += i // mid
        print(lt, rt, mid, result)
        if result >= N:
            results.append(mid)
            lt = mid + 1
        elif result < N:
            rt = mid - 1

    return max(results)


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/2. 랜선자르기/in3.txt", "rt")
    K, N = map(int, input().split())
    data = list()
    [data.append(int(input())) for _ in range(K)]
    print(solve(N, data))