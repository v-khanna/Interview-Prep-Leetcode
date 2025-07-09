"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
"""

from collections import Counter
from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count characters in t
        target_count = Counter(t)
        required = len(target_count)
        formed = 0

        # Sliding window
        left = 0
        min_len = float("inf")
        min_start = 0
        window_count = Counter()

        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1

            # Check if we've formed a valid window
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            # Try to minimize window
            while left <= right and formed == required:
                char = s[left]

                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1

                left += 1

        return s[min_start : min_start + min_len] if min_len != float("inf") else ""


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
    print(solution.minWindow("a", "a"))  # Output: "a"
    print(solution.minWindow("a", "aa"))  # Output: ""
