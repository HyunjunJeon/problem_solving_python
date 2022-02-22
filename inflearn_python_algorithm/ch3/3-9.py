import sys


def solve(N: int, data: list):
    # 1) 맨 위, 맨 아래 [0] 으로 구성된 리스트를 추가
    data.insert(0, [0] * N)
    data.append([0] * N)

    # 2) 각 행의 요소들 맨 앞, 맨 뒤에 0 추가
    for x in data:
        x.insert(0, 0)
        x.append(0)

    # 3) 1개의 숫자가 주어지면 자신의 상-하-좌-우 보다 큰지 작은지 판단
    result = 0
    dx = [-1, 0, 1, 0]  # 12시   6시
    dy = [0, 1, 0, -1]  # 3시    9시

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if all(data[i][j] > data[i + dx[k]][j + dy[k]] for k in range(4)):
                result += 1

    return result


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/8. 곳감/in1.txt", "rt")
    N = int(input())
    data_main = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, data_main))