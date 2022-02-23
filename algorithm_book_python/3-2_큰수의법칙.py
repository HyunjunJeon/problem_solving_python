'''
큰 수의 법칙 풀이 1번, Basic
'''

n, m, k = map(int, input().split())  # 배열크기, 숫자 더해지는 횟수, 인덱스
data = list(map(int, input().split()))

data.sort()  # default=> 오름차순 정렬 -> 큰 수는 맨 뒤에 있을 것
first_max = data[n - 1]
second_max = data[n - 2]

result = 0

while m > 0:
    # 연속 k번 불가능
    for _ in range(k):
        if m == 0: break  # 혹시나 총 횟수가 0이면 바로 탈출
        result += first_max  # 가장 큰 수를 더해줌
        m -= 1  # 총 더한 횟수에서 차감

    # k 번 다 더했을 때 더할 수 있는 수가 없다면(m == 0)
    if m == 0: break

    result += second_max
    m -= 1

print(result)


'''
큰 수의 법칙 풀이 2번, Advanced
m 값의 크기가 100억 이상이어서 시간이 1초 이상 걸리게 된다면?
'''

"""
data = [2,4,5,4,6] 이고 m = 8, k = 3 이라면
정답은 (6+6+6+5) + (6+6+6+5) = 46  
> 수열이 반복되는 것이 특징임

- 반복되는 수열의 크기는 k+1
그럼 반복수열 자체는 총 몇번 등장할까? m / (k+1)

>> 반복 수열 1개의 값을 구하고 * 갯수 하면 끝
"""

recycle_number_list = first_max * k + second_max
result3 = (m / (k+1)) * recycle_number_list
print(result3)

# 책의 Advanced 풀이
count = int(m / (k+1)) * k + m % (k+1)
result2 = 0
result2 += count * first_max
result2 += (m-count) * second_max

print(result2)










