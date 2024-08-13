from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        totalSum = 0

        for i in range(len(nums)):  # Corrected loop
            totalSum += nums[i]

        leftSum = 0

        for i in range(len(nums)):
            if leftSum == (totalSum - leftSum - nums[i]):
                return i
            leftSum += nums[i]

        return -1
