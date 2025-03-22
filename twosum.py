import unittest

def twoSum(nums, target) -> list[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    return [2,3]

class TestLongestSubstring(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(twoSum([1,2,3,0], 3), [2,3])
        self.assertEqual(twoSum([2,7,11,15], 9), [0,1])
        self.assertEqual(twoSum([3,2,4], 6), [1,2])
    


if __name__ == "__main__":
    unittest.main()

