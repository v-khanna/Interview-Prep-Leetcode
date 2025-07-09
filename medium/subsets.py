"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.subsets([1, 2, 3])
    )  # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
