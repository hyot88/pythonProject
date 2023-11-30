# 정규식 a[.]{3,}b 와 매칭되는 문자열은?
import re

pat = re.compile('a[.]{3,}b')

print(pat.match("acccb"))
print(pat.match("a....b"))
print(pat.match("aaaab"))
print(pat.match("a.cccb"))
