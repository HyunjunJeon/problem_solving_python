import sys


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/8. 단어찾기/in2.txt", "rt")
    N = int(input())
    pre_use_word = dict()
    for _ in range(N):
        # 쓰일 단어 N개
        pre_use_word[input()] = 1
    for _ in range(N-1):
        # 쓰인 단어 N-1개
        pre_use_word.pop(input())
    print(list(pre_use_word.keys())[0])