import unittest
from RemoveElement import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.list = [0, 1, 1, 2, 2, 2, 3, 4]
        self.assertEqual(temp.removeElement(self.list, 2), 5)
        self.assertEqual(self.list[0:5], [0, 1, 1, 3, 4])

    def test_no_remove(self):
        temp = Solution()
        self.list = [0, 1, 1, 3, 4, 5, 6, 7]
        self.assertEqual(temp.removeElement(self.list, 2), len(self.list))
        self.assertEqual(self.list, [0, 1, 1, 3, 4, 5, 6, 7])

    def test_all_remove(self):
        temp = Solution()
        self.list = [2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(temp.removeElement(self.list, 2), 0)
        self.assertEqual(self.list, [2, 2, 2, 2, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()
