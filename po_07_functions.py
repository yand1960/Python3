def plus(x: int, y: int) -> int:
    result = x + y
    return result

def minus(x: int = 1, y: int = 0) -> int:
    result = x - y
    return result

def summa(x: int, *args: int) -> int:
    result = x
    for a in args:
        # print(a)
        result += a
    return result

def dummy(x: int, **kwargs):
    for key in kwargs:
        print(key, kwargs[key])

def plus_minus(x: int, y: int) -> [int, int]:
    result1 = x + y
    result2 = x - y
    return result1, result2

if __name__ == "__main__":
    print(plus(1, 2))
    result = plus(1, 2)
    print(result)
    print(plus("a", "b"))

    print(minus(y=2, x=1))
    print(minus(y=3))

    print(summa(123, 22, 33, 44, 55))

    dummy(123, a=1234, aa=2222, c=3333)
    a, b = plus_minus(1, 2)
    print(a)
    print(b)

