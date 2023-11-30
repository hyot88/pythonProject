def mul(m):
    def wrapper(n):
        return m * n
    return wrapper


if __name__ == '__main__':
    mul3 = mul(3)
    mul5 = mul(5)
    print(mul3(10))
    print(mul5(10))
