import sys


def solve(NUM: list, M: int):
    stack = list()
    for x in NUM:
        # 비어있지 않고, 삭제 카운팅이 남아있고, 맨 뒤 숫자보다 현재값이 큰 경우
        while stack and M > 0 and stack[-1] < x:
            stack.pop()
            M -= 1
        stack.append(x)

    if M != 0:
        stack = stack[:-M]

    return "".join(map(str, stack))


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/1. 가장 큰 수/in1.txt", "rt")
    NUM, M = map(str, input().split())
    NUM = list(map(int, NUM))
    M = int(M)
    print(solve(NUM, M))