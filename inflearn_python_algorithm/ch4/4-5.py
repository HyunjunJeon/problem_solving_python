import sys


def solve(N: int, data: list):
    # 회의실은 1개 밖에 없음
    # ** 끝나는 시간을 기준으로 정렬해야, 빨리빨리 끝내고 가장 많은 회의를 할 수 있음 **
    data.sort(key=lambda x: (x[1], x[0]))

    cnt = 1  # 무조건 한번은 회의를 시작하기 때문에
    et = 0
    for start_time, end_time in data:
        if start_time >= et:
            cnt += 1
            et = end_time

    return cnt


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/5. 회의실 배정/in4.txt", "rt")
    N = int(input())
    data = list()
    [data.append(list(map(int, input().split()))) for _ in range(N)]
    print(solve(N, data))