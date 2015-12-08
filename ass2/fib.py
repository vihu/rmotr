''' implementing a memoized recursive fibonacci
'''


class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        self[key] = self.func(*key)
        return self[key]


@memoize
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print fib(50)
    print fib(100)
