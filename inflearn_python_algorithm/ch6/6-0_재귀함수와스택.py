# 재귀함수는 내부적으로 Stack을 활용함(Stack Frame)
# print 문의 위치에 따라서 증가, 감소함 -> Stack에 넣고 그려보면 바로 알게 됌
def DFS(x: int):
    if x > 0:
        DFS(x-1)
        print(x, end=" ")


if __name__ == "__main__":
    n = int(input())
    DFS(n)

