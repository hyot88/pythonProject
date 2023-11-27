f1 = open('text.txt', 'w')
f1.write('Life is too short')
f1.close() # 읽으려면 close 해줘야 한다

f2 = open('text.txt', 'r')
print(f2.read())