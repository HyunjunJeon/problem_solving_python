import sys

sys.stdin = open("/pythonalgorithm_formac/섹션 2/6. 자릿수의 합/in1.txt", "rt")

N = int(input())
a = list(map(int, input().split()))

def digit_sum(x): # 몫 과 나머지 방식
    sum = 0
    while x > 0:
        sum += x % 10 # 자리수의 합
        x = x // 10    # x는 몫으로 변환
    return sum

def digit_sum_str(x): # 문자열로 처리
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -1
for x in a:
    tot = digit_sum_str(x)
    if tot > max:
        max = tot
        res = x

print(res)
