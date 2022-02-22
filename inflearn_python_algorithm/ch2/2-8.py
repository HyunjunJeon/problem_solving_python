import sys
import math


def reverse_num(number):
    num = number[::-1]
    return int(num)


def is_prime(number):
    sqrt_n = math.sqrt(number)
    for i in range(2, int(sqrt_n)):
        if number % i == 0:
            return False
    return True


def solve(n):
    m = reverse_num(n)
    if is_prime(m):
        print(m, end=" ")


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 2/8. 뒤집은 소수/in2.txt", "rt")

    N = int(input())
    M = map(str, input().split())
    for data in M:
        solve(data)