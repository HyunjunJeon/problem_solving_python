import sys


def solve(data: list, N: int):
    s = e = N // 2
    result = 0
    for i in range(N):
        for j in range(s, e + 1):
            result += data[i][j]
        if i < N // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    return result


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/7. 사과나무/in3.txt", "rt")
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(solve(data, N))
