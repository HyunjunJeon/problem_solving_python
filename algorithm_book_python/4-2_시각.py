h = int(input())

count = 0

for i in range(24): # 시
    for j in range(60): # 분
        for k in range(60): # 초
            # 문자열로 바꿔서 3이 있는지 조사 후 count 에 합치기
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)