import sys


def solve(pipe: str):
    stack = list()
    res = 0
    for i in range(len(pipe)):
        if pipe[i] == '(':
            stack.append(pipe[i])
        else:
            stack.pop()
            if pipe[i-1] == '(':
                res += len(stack)
            else:
                res += 1
    return res


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/2. 쇠막대기/in2.txt", "rt")
    pipe = str(input())
    print(solve(pipe))