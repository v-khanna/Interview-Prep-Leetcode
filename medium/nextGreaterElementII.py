"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        # Process twice to handle circular nature
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]
            stack.append(idx)

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreaterElements([1, 2, 1]))  # Output: [2,-1,2]
    print(solution.nextGreaterElements([1, 2, 3, 4, 3]))  # Output: [2,3,4,-1,4]
