import sys


def solve(N:int, M:int, data:list):
    # DVD 크기는 1 ~ 담긴 곡의 합 까지 가능
    lt = 1
    rt = sum(data)
    results = list()

    while lt <= rt:
        mid = (lt + rt) // 2
        ##
        chk = 1  # 무조건 1장에는 다 들어갈 수 있으므로
        music_sum = 0
        for i in data:
            if music_sum + i > mid:
                chk += 1
                music_sum = i
            else:
                music_sum += i
        ##
        if mid >= max(data) and chk <= M:  # DVD 용량은 노래들 중 가장 긴 노래 1개는 최소한 담을 수 있어야 함
            results.append(mid)
            rt = mid - 1
        else:
            lt = mid + 1

    return min(results)


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/3. 뮤직비디오/in4.txt", "rt")
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    print(solve(N, M, data))