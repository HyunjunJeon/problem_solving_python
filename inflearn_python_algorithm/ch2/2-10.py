import sys


def solve(datas):
    sum = 0
    check = 0
    for data in datas:
        if data == 1:
            check += 1
            sum += check
        elif data == 0:
            check = 0
    return sum


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 2/10. 점수 계산/in4.txt", "rt")
    N = int(input())
    print(solve(list(map(int, input().split()))))
