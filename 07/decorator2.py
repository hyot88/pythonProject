import time


def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행 시간: %f" % (end - start))
        return result
    return wrapper


@elapsed
def myFunc(msg):
    """데코레이터 확인 함수"""
    print("'%s'을 출력합니다." % msg)


myFunc("You need python")

