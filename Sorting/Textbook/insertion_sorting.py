array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1): # 해당 인덱스의 왼쪽 부분 (이미 정렬된 부분)과 비교해보자
            if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
                array[j], array[j-1] = array[j-1], array[j]
            else: # 왼쪽으로 이동하면 안 될 경우 (더 작은 수를 만나면)
                break
    return array