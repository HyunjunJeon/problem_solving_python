import sys


def solve(datas: list, check: int):
    lt = 0
    rt = 1
    tot = datas[0]
    result = 0

    while True:
        if tot < check:
            if rt < len(datas):
                tot += datas[rt]
                rt += 1
            else:
                break
        elif tot == check:
            result += 1
            tot -= datas[lt]
            lt += 1
        else:
            tot -= datas[lt]
            lt += 1
    return result


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/5. 수들의 합/in4.txt", "rt")
    N, M = map(int, input().split())
    datas = list(map(int, input().split()))
    print(solve(datas, M))
