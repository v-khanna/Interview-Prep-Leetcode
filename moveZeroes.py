class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        lastNonZeroPosition = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroPosition], nums[i] = nums[i], nums[lastNonZeroPosition]
                lastNonZeroPosition += 1
