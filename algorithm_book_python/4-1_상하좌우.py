# n = int(input()) # 5
n = 5
# plans = input().split() # R R R U D D
plans = ["R","R","R","U","D","D"]

x, y = 1, 1

# L, R, U, D 에 따른 이동
# 왼쪽 위에서 시작, 오른쪽 아래로 갈 때
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

# 왼쪽 아래에서 시작해서 오른쪽 위로 간다면?
'''
이걸 그려놓는게 더 중요함
L: (-1, 0)
R: (1, 0)
U: (0, 1)
D: (0, -1)
'''
dx2 = [-1, 1, 0, 0]
dy2 = [0, 0, 1, -1]

for plan in plans:
    # 이동 후의 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue

            print(f"nx = {nx} , ny = {ny}")
            x, y = nx, ny