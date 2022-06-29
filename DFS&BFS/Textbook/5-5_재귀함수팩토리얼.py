def factorial_recursive(n):
    if n == 1:
        return 1
    return factorial_recursive(n-1)*n

print(factorial_recursive(5))

def recursive_function(i):
    print(f'{i}번 째 재귀함수 시행')
    if i == 1:
        return
    print(f'{i}번 째 재귀함수에서, {i-1}번 째 재귀함수를 실행')
    recursive_function(i-1)
    print(f'{i}번 째 재귀함수 종료')

print(recursive_function(20))