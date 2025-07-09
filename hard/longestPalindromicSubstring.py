"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Expand around center approach
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2:
            return s

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            palindrome1 = expandAroundCenter(i, i)
            # Even length palindrome
            palindrome2 = expandAroundCenter(i, i + 1)

            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(solution.longestPalindrome("cbbd"))  # Output: "bb"
    print(solution.longestPalindrome("a"))  # Output: "a"
