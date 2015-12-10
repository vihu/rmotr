import unittest


class OperationInvalidException(Exception):
    pass


class Operation(object):
    def __init__(self, *args):
        self.args = args

    def operate(self):
        return NotImplementedError


class AddOperation(Operation):
    # The only method present in this class
    def operate(self):
        return sum(self.args)


class SubtractOperation(Operation):
    # The only method present in this class
    def operate(self):
        if self.args:
            return self.args[0] - sum(self.args[1:])
        else:
            return 0


class Calculator(object):
    def __init__(self, **kwds):
        self.ops = kwds

    def calculate(self, *args):
        if args[-1] == 'add':
            return self.ops['operations']['add'](*args[:-1]).operate()
        elif args[-1] == 'subtract':
            return self.ops['operations']['subtract'](*args[:-1]).operate()
        else:
            raise OperationInvalidException


class CalculatorTestCase(unittest.TestCase):
    def test_calculator_with_one_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)

    def test_calculator_with_multiple_operations(self):
        calc = Calculator(
            operations={
                'add': AddOperation,
                'subtract': SubtractOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)
        res = calc.calculate(13, 3, 7, 'subtract')
        self.assertEqual(res, 3)

    def test_calculator_invoked_with_an_invalid_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        with self.assertRaises(OperationInvalidException):
            calc.calculate(1, 5, 13, 2, 'INVALID')


class SubtractOperationTestCase(unittest.TestCase):
    def test_subtract_operation_with_multiple_arguments(self):
        op = SubtractOperation(10, 1, 3, 2, 1)
        self.assertEqual(op.operate(), 3)

    def test_subtract_operation_with_1_arguments(self):
        op = SubtractOperation(5)
        self.assertEqual(op.operate(), 5)

    def test_subtract_operation_negative_result(self):
        op = SubtractOperation(5, 3, 3)
        self.assertEqual(op.operate(), -1)

    def test_subtract_operation_with_no_arguments(self):
        op = SubtractOperation()
        self.assertEqual(op.operate(), 0)


class AddOperationTestCase(unittest.TestCase):
    def test_add_operation_with_multiple_arguments(self):
        op = AddOperation(5, 1, 8, 3, 2)
        self.assertEqual(op.operate(), 19)

    def test_add_operation_with_1_arguments(self):
        op = AddOperation(5)
        self.assertEqual(op.operate(), 5)

    def test_add_operation_with_no_arguments(self):
        op = AddOperation()
        self.assertEqual(op.operate(), 0)


if __name__ == '__main__':
    unittest.main()
