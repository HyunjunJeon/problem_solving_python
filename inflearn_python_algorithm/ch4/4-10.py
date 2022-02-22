import sys


def solve_1(N: int, data: list):
    # 역수열을 만들어보자
    result = list()
    for i in range(1, N + 1):
        cnt = 0
        for j in range(data.index(i)):
            if data[j] > i:
                cnt += 1
        result.append(cnt)

    return result


def solve_2(N: int, data: list):
    # (메인 문제) 역수열로 원수열 만들기
    sequence = [0] * N
    for i in range(N):
        for j in range(N):
            if data[i] == 0 and sequence[j] == 0:
                sequence[j] = i + 1
                break
            elif sequence[j] == 0:
                data[i] -= 1
    return sequence


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/10. 역수열/in1.txt", "rt")
    N = int(input())
    data = list(map(int, input().split()))
    for x in solve_2(N, data):
        print(x, end=" ")

    # 원수열로 역수열 만들 떄 사용
    # N = 8
    # data = [4, 8, 6, 2, 5, 1, 3, 7]
    # print(solve_1(N, data))
