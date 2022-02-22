import sys


def my_solve(data: list):
    result = "YES"

    # 1) 각 행에 1 ~ 9까지 숫자가 중복 없이 나오는가
    # 2) 각 열에 1~9까지 숫자가 중복 없이 나오는가
    for i in range(9):
        check_column = set()
        check_row = set(data[i])
        for j in range(9):
            check_column.add(data[i][j])
        if len(check_row) != 9 or len(check_column) != 9:
            return "NO"

    # 3) 3 x 3 으로 쪼개었을 때, 1~9 숫자가 중복 없이 나오는가
    check1 = set()
    check2 = set()
    check3 = set()

    for i in data[0:3]:
        [check1.add(j) for j in i[0:3]]
        [check2.add(j) for j in i[3:6]]
        [check3.add(j) for j in i[6:9]]
    if len(check1) != 9 or len(check2) != 9 or len(check3) != 9:
        return "NO"

    check1.clear()
    check2.clear()
    check3.clear()

    for i in data[3:6]:
        [check1.add(j) for j in i[0:3]]
        [check2.add(j) for j in i[3:6]]
        [check3.add(j) for j in i[6:9]]
    if len(check1) != 9 or len(check2) != 9 or len(check3) != 9:
        return "NO"

    check1.clear()
    check2.clear()
    check3.clear()

    for i in data[6:9]:
        [check1.add(j) for j in i[0:3]]
        [check2.add(j) for j in i[3:6]]
        [check3.add(j) for j in i[6:9]]
    if len(check1) != 9 or len(check2) != 9 or len(check3) != 9:
        return "NO"

    return result


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/10. 스도쿠 검사/in1.txt", "rt")
    data = [list(map(int, input().split())) for _ in range(9)]
    print(my_solve(data))
