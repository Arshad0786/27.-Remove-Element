class Solution:
    def removeElement(self, nums, val):
        NewArrayPointer = 0
        for OldArrayPointer in range(len(nums)):
            if(nums[OldArrayPointer] != val):
                nums[NewArrayPointer] = nums[OldArrayPointer]
                NewArrayPointer = NewArrayPointer + 1
        return NewArrayPointer