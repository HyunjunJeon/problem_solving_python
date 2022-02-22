import sys


def solve(N: int, data: list):
    data.sort(reverse=True) # 키, 몸무게 둘 중 뭘로 정렬해도 상관없음 => '키' 내림차순 => 몸무게만 비교해보면 됌

    cnt = 1
    ht = data[0][0]
    wt = data[0][1]

    print(data)

    for h, w in data:
        if w > wt:
            cnt += 1
            wt = w

    return cnt


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/6. 씨름선수/in5.txt", "rt")
    N = int(input())
    data = list()
    [data.append(list(map(int, input().split()))) for _ in range(N)]
    print(solve(N, data))


