result = 0

try:
    a = {'A':90, 'B':80}
    result = a['C']
except KeyError:
    result = 70

print(result)


### 찐 답

a = {'A':90, 'B':80}
result = a.get('C', 70)
print(result)