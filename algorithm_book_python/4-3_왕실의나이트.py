now = input()
row = int(now[1])
column = int(ord(now[0]) - ord('a')) + 1  # 숫자 1~ 로 컬럼을 맞춰줌

# L자로 이동하는 모든 경우의 수 표시
# 수평2칸(왼-오), 수직1칸(위-아래) / 수직2칸(위-아래), 수평1칸(왼-오)
night_steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2)]

# 이동 가능한 모든 수를 계산함
result = 0
for steps in night_steps:
    # 이동
    nx = column + steps[0]
    ny = row + steps[1]

    # 이동 시킨 점이 8 by 8 격자 안에 존재하는지
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        result += 1

print(result)