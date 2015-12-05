''' implementing a memoized recursive factorial
'''
import time
from functools import wraps


class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        self[key] = self.func(*key)
        return self[key]


def timer(func):
    @wraps(func)
    def timing_func(*args, **kwargs):
        start = time.time()
        answer = func(*args, **kwargs)
        end = time.time()
        print 'Took {t} to calculate {f}'.format(t=end-start,
                                                 f=func.__name__)
        return answer
    return timing_func


@memoize
@timer
def mfactorial(n):
    if n in [0, 1]:
        return 1
    return n * mfactorial(n-1)


print mfactorial(20)
