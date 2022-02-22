import sys


def count_horse(distance: int, data: list):
    # 1마리는 무조건 lt 쪽에 위치하기 때문에 초기값 셋팅이 이렇게 됌
    horse_cnt = 1
    end_point = data[0]

    # 나머지 마구간들을 돌면서 거리 비교해서 distance 보다 크거나 같다면 말을 배치함
    for i in range(1, N):
        if data[i] - end_point >= distance:
            horse_cnt += 1
            end_point = data[i]

    return horse_cnt


def solve(N: int, C: int, data: list):
    result = 0
    data.sort()
    # 1 ~ max(data) 까지 마구간끼리의 거리
    lt = 1
    rt = data[N-1]  # 정렬했으니까 마지막 요소가 제일 큰 것
    while lt <= rt:
        mid = (lt + rt) // 2
        if count_horse(mid, data) >= C:
            result = mid
            lt = mid + 1
        else:
            rt = mid - 1
    return result


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/4. 마구간 정하기/in1.txt", "rt")
    N, C = map(int, input().split())
    data = list()
    [data.append(int(input())) for _ in range(N)]
    print(solve(N, C, data))
