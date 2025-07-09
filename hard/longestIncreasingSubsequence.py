"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""

from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Binary search approach - O(n log n)
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)

    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        # DP approach - O(n²)
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
    print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # Output: 4
    print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # Output: 1
