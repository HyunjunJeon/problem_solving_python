import sys


def solve(N: int, data: list):
    cnt = 0
    last = 0
    results = ""
    tmp = list()

    lt = 0
    rt = N-1

    # tuple 자료형에 넣고 정렬해주는 방식
    while lt <= rt:
        if data[lt] > last:
            tmp.append((data[lt], "L"))
        if data[rt] > last:
            tmp.append((data[rt], "R"))
        tmp.sort(key=lambda x: x[0])
        if len(tmp) == 0:
            break
        else:
            if tmp[0][1] == 'L':
                lt += 1
            else:
                rt -= 1
            results += tmp[0][1]
            last = tmp[0][0]
            tmp.clear()
            cnt += 1

    print(cnt)
    print(results)


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 4/9. 증가수열 만들기/in1.txt", "rt")
    N = int(input())
    data = list(map(int, input().split()))
    solve(N, data)