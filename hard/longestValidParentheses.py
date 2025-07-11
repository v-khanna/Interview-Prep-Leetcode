"""
Longest Valid Parentheses (Hard)
https://leetcode.com/problems/longest-valid-parentheses/

Problem: Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example:
Input: s = ")()())"
Output: 4

Approach: Stack and Dynamic Programming
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        Find longest valid parentheses using stack
        """
        if not s:
            return 0

        stack = [-1]  # Initialize with -1 to handle edge cases
        max_length = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length

    def longestValidParenthesesDP(self, s):
        """
        Dynamic programming approach
        """
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        max_length = 0

        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    # Case: "()"
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    # Case: "((...))"
                    dp[i] = (
                        dp[i - 1]
                        + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                        + 2
                    )

                max_length = max(max_length, dp[i])

        return max_length

    def longestValidParenthesesTwoPass(self, s):
        """
        Two-pass approach without extra space
        """
        if not s:
            return 0

        max_length = 0

        # Left to right pass
        left = right = 0
        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, 2 * right)
            elif right > left:
                left = right = 0

        # Right to left pass
        left = right = 0
        for char in reversed(s):
            if char == "(":
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left = right = 0

        return max_length

    def longestValidParenthesesOptimized(self, s):
        """
        Optimized version with early termination
        """
        if not s:
            return 0

        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)

        return max_length


def test_longest_valid_parentheses():
    """Test cases for Longest Valid Parentheses"""
    solution = Solution()

    # Test case 1: Basic case
    s1 = ")()())"
    assert solution.longestValidParentheses(s1) == 4
    assert solution.longestValidParenthesesDP(s1) == 4
    assert solution.longestValidParenthesesTwoPass(s1) == 4
    assert solution.longestValidParenthesesOptimized(s1) == 4

    # Test case 2: Simple valid parentheses
    s2 = "(()"
    assert solution.longestValidParentheses(s2) == 2
    assert solution.longestValidParenthesesDP(s2) == 2
    assert solution.longestValidParenthesesTwoPass(s2) == 2
    assert solution.longestValidParenthesesOptimized(s2) == 2

    # Test case 3: Empty string
    s3 = ""
    assert solution.longestValidParentheses(s3) == 0
    assert solution.longestValidParenthesesDP(s3) == 0
    assert solution.longestValidParenthesesTwoPass(s3) == 0
    assert solution.longestValidParenthesesOptimized(s3) == 0

    # Test case 4: All invalid
    s4 = "((("
    assert solution.longestValidParentheses(s4) == 0
    assert solution.longestValidParenthesesDP(s4) == 0
    assert solution.longestValidParenthesesTwoPass(s4) == 0
    assert solution.longestValidParenthesesOptimized(s4) == 0

    # Test case 5: Complex nested
    s5 = "((()))"
    assert solution.longestValidParentheses(s5) == 6
    assert solution.longestValidParenthesesDP(s5) == 6
    assert solution.longestValidParenthesesTwoPass(s5) == 6
    assert solution.longestValidParenthesesOptimized(s5) == 6

    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_valid_parentheses()
