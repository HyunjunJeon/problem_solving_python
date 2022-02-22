import sys


def solve(data: list, N: int):
    global sum
    result = 0

    # 각 행의 합
    max_row = 0
    for i in data:
        temp_sum = sum(i)
        if max_row < temp_sum:
            max_row = temp_sum # 각 리스트 의 합으로 나올 것

    # 각 열의 합
    max_column = 0
    for i in range(N):
        sum_c = 0
        for j in range(N):
            sum_c += data[i][j]

        if max_column < sum_c:
            max_column = sum_c

    # 두 대각선의 합
    max_diagonal = 0
    temp_sum = 0
    for i in range(N):
        temp_sum += data[i][i]

    if max_diagonal < temp_sum:
        max_diagonal = temp_sum

    temp_sum = 0
    for j in range(N-1, -1, -1):
        temp_sum += data[(N-1)-j][j]

    if max_diagonal < temp_sum:
        max_diagonal = temp_sum

    return max(max_row, max_column, max_diagonal)


def solve2(data: list, N: int):
    max_row = max_column = max_diagonal = 0
    for i in range(N):
        sum_row = sum_column = 0
        for j in range(N):
            sum_row += data[i][j]
            sum_column += data[j][i]
        if sum_row > max_row:
            max_row = sum_row
        if sum_column > max_column:
            max_column = sum_column

    sum_diagonal1 = sum_diagonal2 = 0
    for i in range(N):
        sum_diagonal1 += data[i][i]
        sum_diagonal2 += data[i][(N-1)-i]

    max_diagonal = max(sum_diagonal1, sum_diagonal2)

    return max(max_row, max_column, max_diagonal)

if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/6. 격자판 최대합/in3.txt", "rt")
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(solve(data, N))