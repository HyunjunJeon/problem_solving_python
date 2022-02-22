import sys


def change_list(original_list: list, start: int, end: int):
    # 파이썬 List의 slicing 의 경우 [숫자: 숫자] 는 바로 사용되는데 그 이외에는 slice 객체를 이용해야함
    # Ex> 지금 문제처럼 변수 할당으로 해결하려는 경우 => original_list[slice(start, end)]

    # 원래 리스트의 지정된 인덱스 부분에, 원래 리스트에서 뒤집에서 만들어준 부분을 붙임
    original_list[slice(start-1, end)] = list(reversed(original_list[slice(start - 1, end)]))

    return original_list


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/3. 카드 역배치/in1.txt", "rt")
    data = [i for i in range(1, 21)]
    for _ in range(10):
        a, b = map(int, input().split())
        data = change_list(data, a, b)
    print(data)
