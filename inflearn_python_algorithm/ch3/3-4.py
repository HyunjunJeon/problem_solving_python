import sys


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 3/4. 두 리스트 합치기/in1.txt", "rt")
    N = input() # 버리는 인풋
    list1 = list(map(int, input().split()))
    M = input() # 버리는 인풋
    list2 = list(map(int, input().split()))

    list3 = list1 + list2
    list3.sort()
    print(list3)