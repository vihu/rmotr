import unittest


class OperationInvalidException(Exception):
    pass


class Operation(object):
    def __init__(self, *args):
        self.args = args

    def operate(self):
        return NotImplementedError


class AddOperation(Operation):
    def __init__(self, *args):
        super(AddOperation, self).__init__(*args)

    # The only method present in this class
    def operate(self):
        return sum(self.args)


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