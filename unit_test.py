import unittest
from RemoveElement import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.list = [0, 1, 1, 2, 2, 2, 3, 4]
        self.assertEqual(temp.removeElement(self.list,2),5)


if __name__ == "__main__":
    unittest.main()