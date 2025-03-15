import unittest
from listnode import addTwoNumbers, ListNode

def list_to_linked_list(lst):
    """Helper function to convert a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    """Helper function to convert a linked list to a list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class TestAddTwoNumbers(unittest.TestCase):
    def test_case_1(self):
        """Test case: [2,4,3] + [5,6,4] = [7,0,8]"""
        l1 = list_to_linked_list([2,4,3])
        l2 = list_to_linked_list([5,6,4])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [7,0,8])

    def test_case_2(self):
        """Test case: [0] + [0] = [0]"""
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [0])

    def test_case_3(self):
        """Test case: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]"""
        l1 = list_to_linked_list([9,9,9,9,9,9,9])
        l2 = list_to_linked_list([9,9,9,9])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [8,9,9,9,0,0,0,1])

if __name__ == '__main__':
    unittest.main()