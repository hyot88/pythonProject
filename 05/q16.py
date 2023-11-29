import itertools

data = ['a', 'b', 'c', 'd']
arr = list(itertools.permutations(data, 4))

for i in arr:
    print(''.join(i), end=' ')

print('\n')
print(len(list(itertools.permutations(data, 4))))