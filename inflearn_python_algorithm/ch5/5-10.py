import sys
import heapq


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/10. 최소힙/in3.txt", "rt")
    heap = list()
    while True:
        data = int(input())
        if data == -1:
            break
        elif data == 0:
            if len(heap) > 0:
                print(heapq.heappop(heap))
            else:
                print(-1)
        else:
            heapq.heappush(heap, data)