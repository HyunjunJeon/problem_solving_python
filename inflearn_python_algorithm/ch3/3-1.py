import sys


def is_palindrom(word:str):
    result = "NO"
    word = word.upper()

    if word == word[::-1]:
        result = "YES"

    return result


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/1. 회문 문자열 검사/in3.txt", "rt")
    N = int(input())
    for i in range(1, N+1):
        print(f"#{i} {is_palindrom(input())}")
