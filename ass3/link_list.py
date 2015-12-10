"""
A Linked List (https://en.wikipedia.org/wiki/Linked_list) is a linear data structure.
You can think of it as an implementation of a regular Python List.

Using Object Oriented programming, build a simple Linked List that shares the same
interface with Python Lists:

    l = LinkedList()

    l.append(2)
    l.count()  # Should return 1

    l + [2, 3]     # Should return [1, 2, 3] but not mutate the original list
    l += [3, 4]   # Should return None and append [3, 4] to the original list

    l.pop(0)       # Should remove and return the first element.

    # Important. This should be True:
    LinkedList([1, 2, 3]) == LinkedList([1, 2, 3])

To ease your task, a LinkedList is constructed using different Nodes. Each node
has a reference to other Node, what makes it a recursive class, it'll point to itself.

"""
import unittest


class Node(object):
    pass


class LinkedList(object):
    pass


class LinkedListTestCase(unittest.TestCase):
    ListImplementationClass = LinkedList

    def test_creation_and_equal(self):
        l1 = self.ListImplementationClass([1, 2, 3])

        self.assertTrue(l1.start is not None)
        self.assertEqual(l1.start.elem, 1)

        self.assertTrue(l1.end is not None)
        self.assertEqual(l1.end.elem, 3)

        self.assertTrue(l1.start.next is not None)
        self.assertEqual(l1.start.next.elem, 2)

        self.assertTrue(l1.start.next.next is not None)
        self.assertEqual(l1.start.next.next.elem, 3)

    def test_append(self):
        my_list = self.ListImplementationClass()

        my_list.append(1)
        self.assertEqual(my_list.start.elem, 1)
        self.assertEqual(my_list.start.next, None)
        self.assertEqual(my_list, self.ListImplementationClass([1]))

        my_list.append(2)
        self.assertEqual(my_list.start.elem, 1)
        self.assertEqual(my_list.start.next, Node(2))
        self.assertEqual(my_list.start.next.elem, 2)
        self.assertEqual(my_list.start.next.next, None)

        self.assertEqual(my_list.count(), 2)

    def test_count(self):
        self.assertEqual(self.ListImplementationClass([1, 2, 3]).count(), 3)

    def test_pop_removes_last_item_by_default(self):
        l1 = self.ListImplementationClass([1, 2, 3])

        elem = l1.pop()
        self.assertEqual(elem, 3)
        self.assertEqual(l1.count(), 2)
        self.assertEqual(l1, self.ListImplementationClass([1, 2]))

    def test_pop_removes_first_item(self):
        l1 = self.ListImplementationClass([1, 2, 3])

        elem = l1.pop(0)
        self.assertEqual(elem, 1)
        self.assertEqual(l1.count(), 2)
        self.assertEqual(l1, self.ListImplementationClass([2, 3]))

    def test_pop_removes_last_item(self):
        l1 = self.ListImplementationClass([1, 2, 3])

        elem = l1.pop(2)
        self.assertEqual(elem, 3)
        self.assertEqual(l1.count(), 2)
        self.assertEqual(l1, self.ListImplementationClass([1, 2]))

    def test_pop_removes_item_in_the_middle_of_the_list(self):
        l1 = self.ListImplementationClass([1, 2, 3, 4, 5])

        elem = l1.pop(2)
        self.assertEqual(elem, 3)
        self.assertEqual(l1.count(), 4)
        self.assertEqual(l1, self.ListImplementationClass([1, 2, 4, 5]))

        elem = l1.pop(1)
        self.assertEqual(elem, 2)
        self.assertEqual(l1.count(), 3)
        self.assertEqual(l1, self.ListImplementationClass([1, 4, 5]))

    def test_pop_with_a_single_element_list(self):
        # Default index
        l1 = self.ListImplementationClass([9])

        elem = l1.pop()
        self.assertEqual(elem, 9)
        self.assertEqual(l1.count(), 0)
        self.assertEqual(l1, self.ListImplementationClass([]))

        # index == 0
        l1 = self.ListImplementationClass([9])

        elem = l1.pop(0)
        self.assertEqual(elem, 9)
        self.assertEqual(l1.count(), 0)
        self.assertEqual(l1, self.ListImplementationClass([]))

    def test_pop_raises_an_exception_with_empty_list(self):
        with self.assertRaises(IndexError):
            self.ListImplementationClass().pop()

        with self.assertRaises(IndexError):
            self.ListImplementationClass().pop(0)

        with self.assertRaises(IndexError):
            self.ListImplementationClass().pop(3)

    def test_pop_raises_an_exception_with_invalid_index(self):
        with self.assertRaises(IndexError):
            self.ListImplementationClass([1]).pop(1)

        with self.assertRaises(IndexError):
            self.ListImplementationClass([1, 2, 3]).pop(3)

    def test_equals(self):
        self.assertEqual(
            self.ListImplementationClass([1, 2, 3]),
            self.ListImplementationClass([1, 2, 3]))

        self.assertEqual(
            self.ListImplementationClass([]),
            self.ListImplementationClass([]))

        self.assertEqual(
            self.ListImplementationClass([1]),
            self.ListImplementationClass([1]))

        self.assertNotEqual(
            self.ListImplementationClass([1, 2]),
            self.ListImplementationClass([1, 2, 3]))

        self.assertNotEqual(
            self.ListImplementationClass([1]),
            self.ListImplementationClass([]))

    def test_add_list(self):
        my_list = self.ListImplementationClass()
        new_list = my_list + self.ListImplementationClass([1])
        self.assertEqual(new_list, self.ListImplementationClass([1]))
        self.assertEqual(my_list, self.ListImplementationClass())

        my_list = self.ListImplementationClass([1, 2])
        new_list = my_list + self.ListImplementationClass([3, 4])
        self.assertEqual(new_list, self.ListImplementationClass([1, 2, 3, 4]))
        self.assertEqual(my_list, self.ListImplementationClass([1, 2]))

        my_list = self.ListImplementationClass([1, 2])
        new_list = my_list + self.ListImplementationClass()
        self.assertEqual(new_list, self.ListImplementationClass([1, 2]))
        self.assertEqual(my_list, self.ListImplementationClass([1, 2]))

        my_list = self.ListImplementationClass()
        new_list = my_list + self.ListImplementationClass()
        self.assertEqual(new_list, self.ListImplementationClass())
        self.assertEqual(new_list.count(), 0)
        self.assertEqual(my_list, self.ListImplementationClass())
        self.assertEqual(my_list.count(), 0)

    def test_str(self):
        my_list = self.ListImplementationClass([1, 2, 3])
        self.assertEqual(str(my_list), "[1, 2, 3]")

        my_list = self.ListImplementationClass()
        self.assertEqual(str(my_list), "[]")

        my_list = self.ListImplementationClass([])
        self.assertEqual(str(my_list), "[]")

    def test_add_equals_list(self):
        my_list = self.ListImplementationClass()
        my_list += self.ListImplementationClass([1, 2])
        self.assertEqual(my_list, self.ListImplementationClass([1, 2]))

        my_list = self.ListImplementationClass([1, 2])
        my_list += self.ListImplementationClass([3, 4])
        self.assertEqual(my_list, self.ListImplementationClass([1, 2, 3, 4]))

        my_list = self.ListImplementationClass([1, 2])
        my_list += self.ListImplementationClass()
        self.assertEqual(my_list, self.ListImplementationClass([1, 2]))

        my_list = self.ListImplementationClass()
        my_list += self.ListImplementationClass()
        self.assertEqual(my_list.count(), 0)
        self.assertEqual(my_list, self.ListImplementationClass())


if __name__ == '__main__':
    unittest.main()
