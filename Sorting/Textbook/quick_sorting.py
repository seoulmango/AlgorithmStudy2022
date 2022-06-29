array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면, 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
            print('피벗이 교체됨:\n', array)
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]
            print('좌우가 교체됨:\n', array)

    
    # 분할 이후 왼쪽 부분
    print('\n 왼쪽 부분 정렬 시행')
    quick_sort(array, start, right-1)
    # 분할 이후 오른쪽 부분
    print('\n 오른쪽 부분 정렬 시행')
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)

print(array)