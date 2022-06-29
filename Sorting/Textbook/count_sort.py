# 모든 원소의 값이 0 이상이라고 가정한다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(array)+1)
# count = [0의 개수, 1의 개수, 2의 개수, ... , 9의 개수]

for i in range(len(array)):
    # 해당 숫자의 인덱스의 값 증가
    count[array[i]] += 1

    # count = [0의 개수 = 2, 1의 개수 = 2, 2의 개수 = 2, ... , 9의 개수 = 2]


for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=' ')
