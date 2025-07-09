"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_map = {}
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            else:
                max_length = max(max_length, end - start + 1)

            char_map[char] = end

        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))  # Output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))  # Output: 3
