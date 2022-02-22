import sys


def my_solve(data: list):
    result = 0

    for i in range(3):
        for j in range(7):
            temp = data[j][i: (5 + i)]
            if temp == temp[::-1]:  # ROW 검증
                result += 1
            for k in range(int(5//2)):
                if data[i + k][j] != data[i + 5 - k - 1][j]: # COLUMN 검증
                    break
            else:
                result += 1

    return result


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/11. 격자판 회문수/in1.txt", "rt")
    data = [list(map(int, input().split())) for _ in range(7)]
    print(my_solve(data))
