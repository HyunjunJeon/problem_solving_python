n, k = map(int, input().split())

# 1) N에서 1을 뺀다
# 2) N을 K로 나눈다(나누어 떨어질 때만)
result = 0
# 내 풀이: 단순하게 루프안에서 조건대로 (N <= 10만 이하니까 복잡도 측면에서 괜찮음)
while True:
    if n == 1:
        break
    if n % k == 0:
        n = n / k
    else:
        n -= 1
    result += 1
print(result)

# 책의 Advanced 풀이
# N이 K의 배수가 될 때까지 한번에 - 시켜버림
result_2 = 0
while True:
    # n == k 로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result_2 += (n - target)
    n = target

    # n 이 k보다 작아서 더이상 나눌 수 없을 때 break
    if n < k:
        break

    n //= k
    result_2 += 1

# 이렇게 나온 결과는 n < k 인 어떤 수 일거임
result_2 += (n - 1)  # 마지막으로 1 이 될때까지는 빼는 것밖에 할 수 없음(n < k 니까 나누기 불가)
print(result_2)


