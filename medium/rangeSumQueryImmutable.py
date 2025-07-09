"""
Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Test cases
if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sumRange(0, 2))  # Output: 1
    print(obj.sumRange(2, 5))  # Output: -1
    print(obj.sumRange(0, 5))  # Output: -3
