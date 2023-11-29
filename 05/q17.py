import itertools

students = ['김승현', '김진호', '강춘자', '이예준', '김현주']
work = ['청소', '빨래', '설거지']

result = itertools.zip_longest(students, work, fillvalue='휴식')
print(list(result))