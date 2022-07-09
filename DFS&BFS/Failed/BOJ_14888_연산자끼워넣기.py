from itertools import permutations

n = int(input())
numlist = list(input().split())
cal_num = list(map(int, input().split()))

callist = []

callist += ['+'] * cal_num[0]
callist += ['-'] * cal_num[1]
callist += ['*'] * cal_num[2]
callist += ['/'] * cal_num[3]

# 연산자를 나열할 순서들의 경우의 수
cal_order = list(permutations(callist))
cal_order = list(set(cal_order))

# string으로 되어 있는 식을 계산하는 함수
def calculate(equation):
    if '+' in equation:
        a, b = map(float, equation.split('+'))
        return a+b
    elif '*' in equation:
        a, b = map(float, equation.split('*'))
        return a*b
    elif '/' in equation:
        a, b = map(float, equation.split('/'))
        if a<0:
            return -((-a)//b)
        elif a == 0:
            return float('inf')
        return a//b
    elif '-' in equation:
        minus_n = equation.count('-')
        if minus_n == 1:
            a, b = map(float, equation.split('-'))
            return a-b
        elif minus_n == 2:
            if equation[0] == '-':
                a, b = map(float, equation[1:].split('-'))
                a = -a
                return a-b
            else:
                a, blank, b = map(float, equation.split('-'))
                return a+b
        elif minus_n == 3:
            equation.replace('-', ' ')
            blank1, a, blank2, b = map(float, equation.split('-'))
            return (-a)-(-b)
            

results = []
for i in range(len(cal_order)):
    equation = numlist[0]+cal_order[i][0]+numlist[1]
    for j in range(1, len(cal_order[i])):
        nxt_num = str(calculate(equation))
        equation = nxt_num + cal_order[i][j] + numlist[j+1]
    results.append(calculate(equation))

no_inf_results = [result for result in results if result!=float('inf')]
print(int(max(no_inf_results)))
print(int(min(no_inf_results)))