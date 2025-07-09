"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # XOR all numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num

        # Find the rightmost set bit
        rightmost_bit = xor_result & -xor_result

        # Separate numbers into two groups
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([1, 2, 1, 3, 2, 5]))  # Output: [3,5]
    print(solution.singleNumber([-1, 0]))  # Output: [-1,0]
    print(solution.singleNumber([0, 1]))  # Output: [0,1]
