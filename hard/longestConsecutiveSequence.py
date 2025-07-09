"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Only start counting if this is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
    print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
