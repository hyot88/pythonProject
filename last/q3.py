a = [1, 2, 3]
a = a + [4, 5]
print(a)

b = [1, 2, 3]
b = b.extend([4, 5])
print(b)

'''
두개의 차이점은 주소값의 변화이다
+ 로 더하면 새로운 주소에 저장되는데,
extend로 하면 주소가 변경되지 않는다
값을 id로 확인해보면 알 수 있다.
ex) id(a)
'''