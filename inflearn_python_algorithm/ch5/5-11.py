import sys
import heapq


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/11. 최대힙/in1.txt", "rt")
    heap = list()
    while True:
        data = int(input())
        if data == -1:
            break
        elif data == 0:
            if len(heap) > 0:
                print(heapq.heappop(heap)[1])  # 튜플에 넣어놓은 값 중 2번째 원소가 내가 원하는 값이기 때문에
            else:
                print(-1)
        else:
            heapq.heappush(heap, (-data, data))  # 기본이 최소힙이기 때문에, 튜플의 첫번쨰 원소를 우선순위로 힙을 구성함. 그러기 때문에 -로 반대로 해주는 것