"""
Reverse String (Easy)
https://leetcode.com/problems/reverse-string/

Problem: Write a function that reverses a string. The input string is given as an array of characters s.

Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Approach: Two pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def reverseString(self, s):
        """
        Reverse string in-place using two pointers
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseStringRecursive(self, s):
        """
        Reverse string using recursion
        """

        def reverse(left, right):
            if left >= right:
                return

            s[left], s[right] = s[right], s[left]
            reverse(left + 1, right - 1)

        reverse(0, len(s) - 1)

    def reverseStringStack(self, s):
        """
        Reverse string using stack (not in-place)
        """
        stack = []
        for char in s:
            stack.append(char)

        for i in range(len(s)):
            s[i] = stack.pop()

    def reverseStringSlice(self, s):
        """
        Reverse string using slice (not in-place)
        """
        s[:] = s[::-1]


def test_reverse_string():
    """Test cases for Reverse String"""
    solution = Solution()

    # Test case 1: Basic case
    s1 = ["h", "e", "l", "l", "o"]
    solution.reverseString(s1)
    assert s1 == ["o", "l", "l", "e", "h"]

    # Test case 2: Single character
    s2 = ["a"]
    solution.reverseString(s2)
    assert s2 == ["a"]

    # Test case 3: Two characters
    s3 = ["a", "b"]
    solution.reverseString(s3)
    assert s3 == ["b", "a"]

    # Test case 4: Empty array
    s4 = []
    solution.reverseString(s4)
    assert s4 == []

    # Test case 5: Palindrome
    s5 = ["r", "a", "c", "e", "c", "a", "r"]
    solution.reverseString(s5)
    assert s5 == ["r", "a", "c", "e", "c", "a", "r"]

    # Test recursive method
    s6 = ["h", "e", "l", "l", "o"]
    solution.reverseStringRecursive(s6)
    assert s6 == ["o", "l", "l", "e", "h"]

    # Test stack method
    s7 = ["h", "e", "l", "l", "o"]
    solution.reverseStringStack(s7)
    assert s7 == ["o", "l", "l", "e", "h"]

    # Test slice method
    s8 = ["h", "e", "l", "l", "o"]
    solution.reverseStringSlice(s8)
    assert s8 == ["o", "l", "l", "e", "h"]

    print("All test cases passed!")


if __name__ == "__main__":
    test_reverse_string()
