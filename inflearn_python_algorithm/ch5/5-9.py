import sys


def solve(A: str, B: str):
    # 단어 카운팅(대소문자 구별함) 후 비교해야 하는데, 그 구성이 같으면 아나그램 YES 아니면 NO
    check = dict()

    # 넣고
    for i in A:
        check[i] = check.get(i, 0) + 1
    # 빼고
    for j in B:
        check[j] = check.get(j, 0) - 1

    if any(check.values()) > 0:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/9. 아나그램(구글)/in1.txt", "rt")
    A = input()
    B = input()
    print(solve(A, B))