import os
os.chdir('/Users/kakao_ent/PycharmProjects')
temp = os.popen('pwd')
print(temp.read())