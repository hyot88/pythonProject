'''
임의로 만든 .py 를 모듈로 사용하는 방법은 다음과 같다

1. sys 모듈 사용하기
#>>> import sys
#>>> sys.path.append("c:/doit")
#import mymod

2. PYTHONPATH 환경 변수 사용하기
C:\Users\home> set PYTHONPATH=c:\doit
C:\Users\home> python
#>>> import mymod

3. 현재 디렉터리 사용하기
C:\Users\home> cd c:\doit
C:\doit> python
#>>> import mymod
'''