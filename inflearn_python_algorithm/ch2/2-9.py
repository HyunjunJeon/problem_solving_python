import sys


def solve(data):
    i, j, k = data
    sum = 0
    if i == j and j == k:
        sum += 10000 + i * 1000
    elif i != j and j != k and k != i:
        sum += max(i, j, k) * 100
    else:
        if i == j and j != k:
            sum += 1000 + i * 100
        elif j == k and i != k:
            sum += 1000 + j * 100
        else:
            sum += 1000 + k * 100
    return sum


def solve2(data):
    i, j, k = data
    sum = 0
    if i == j and j == k:
        sum += 10000 + i * 1000
    elif i == j or i == k:
        sum += 1000 + i * 100
    elif j == k:
        sum += 1000 + j * 100
    else:
        sum += max(i, j, k) * 100
    return sum


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 2/9. 주사위 게임/in5.txt", "rt")
    N = int(input())
    result = set()
    for _ in range(N):
        data = list(map(int, input().split()))
        result.add(solve2(data))
    print(max(result))