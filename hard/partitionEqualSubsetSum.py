"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.canPartition([1, 5, 11, 5]))  # Output: True
    print(solution.canPartition([1, 2, 3, 5]))  # Output: False
