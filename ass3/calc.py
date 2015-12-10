class Calculator(object):
    def add(self, *args):
        return sum(args)

    def subtract(self, a, b):
        return a-b

    def multiply(self, *args):
        return reduce(lambda x, y: x*y, args)

    def divide(self, a, b):
        try:
            return a/(b + 0.0)
        except ZeroDivisionError:
            return 'Cannot divide by 0'