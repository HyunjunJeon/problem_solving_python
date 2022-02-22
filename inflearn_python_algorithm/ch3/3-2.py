import sys
import re


def count_divisor(num: int):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += 1
    return result


def match_number(string: str):
    pattern = re.compile('[0-9]')
    num_list = pattern.findall(string)
    number = ""
    for num in num_list:
        number += num
    return int(number)


# 임의의 문자열에서 숫자만 꺼내서 다시 수를 만드는 방법( *10은 계속 자리수를 늘려주는거임)
def match_number2(string: str):
    res = 0
    for x in string:
        if x.isdecimal():
            res = res * 10 + int(x)
    return res


def solve(string: str):
    natural_number = match_number(string)
    print(natural_number)
    print(count_divisor(natural_number))


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/2. 숫자만 추출/in1.txt", "rt")
    data = input()
    solve(data)
