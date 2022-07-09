import itertools

n = int(input())
nlist = list(map(int, input().split()))
onum = list(map(int, input().split()))
olist = ['+' for _ in range(onum[0])] + ['-' for _ in range(onum[1])] + ['*' for _ in range(onum[2])]
olist += ['/' for _ in range(onum[3])]
operations = list(itertools.permutations(olist, n-1))

for operation in operations:
    string = ""
    for pair in zip(operation, nlist[1:]):
