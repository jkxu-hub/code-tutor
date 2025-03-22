import unittest

def length_of_longest_substring(s: str) -> int:
    return 0

class TestLongestSubstring(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)
    
    def test_edge_cases(self):
        self.assertEqual(length_of_longest_substring(""), 0)  # Empty string
        self.assertEqual(length_of_longest_substring("a"), 1)  # Single character
        self.assertEqual(length_of_longest_substring("abcdef"), 6)  # All unique
        self.assertEqual(length_of_longest_substring("abba"), 2)  # Repeating pattern
        self.assertEqual(length_of_longest_substring("dvdf"), 3)  # Overlapping sequence
        self.assertEqual(length_of_longest_substring("tmmzuxt"), 5)  # Complex case

if __name__ == "__main__":
    unittest.main()
