import sys


def solve(N: int, data_main:list , M: int, data_sub: list):
    # 1) 주어진 조건대로 돌리기
    for loop in data_sub:
        row = loop[0] - 1
        direction = loop[1]
        cycle = loop[2]
        if direction == 0:  # 왼쪽
            for _ in range(cycle):
                data_main[row].append(data_main[row].pop(0))  # 맨 앞의 자료를 꺼내서 맨 뒤로(Queue)

        else:  # 오른쪽
            for _ in range(cycle):
                data_main[row].insert(0, data_main[row].pop())  # 맨 뒤의 자료를 꺼내서 맨 앞으로(Stack)

    # 2) 모래시계 모양으로 탐색
    result = 0
    s = 0
    e = N
    for i in range(N):
        for j in range(s, e):
            result += data_main[i][j]
        if i < N // 2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1

    return result


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/8. 곳감/in1.txt", "rt")
    N = int(input())
    data_main = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    data_sub = [list(map(int, input().split())) for _ in range(M)]
    print(solve(N, data_main, M, data_sub))