"""
Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

Problem: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example:
Input: s = "anagram", t = "nagaram"
Output: true

Approach: Character counting
Time Complexity: O(n)
Space Complexity: O(1) since alphabet size is fixed
"""


class Solution:
    def isAnagram(self, s, t):
        """
        Check if strings are anagrams using character counting
        """
        if len(s) != len(t):
            return False

        # Count characters in both strings
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        return True

    def isAnagramSort(self, s, t):
        """
        Check if strings are anagrams using sorting
        """
        return sorted(s) == sorted(t)

    def isAnagramCounter(self, s, t):
        """
        Check if strings are anagrams using Counter
        """
        from collections import Counter

        return Counter(s) == Counter(t)

    def isAnagramArray(self, s, t):
        """
        Check if strings are anagrams using fixed-size array
        """
        if len(s) != len(t):
            return False

        # Use array for ASCII characters
        char_count = [0] * 26

        for char in s:
            char_count[ord(char) - ord("a")] += 1

        for char in t:
            char_count[ord(char) - ord("a")] -= 1
            if char_count[ord(char) - ord("a")] < 0:
                return False

        return True

    def isAnagramOptimized(self, s, t):
        """
        Optimized version with early termination
        """
        if len(s) != len(t):
            return False

        char_count = {}

        # Count characters in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Check characters in t
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        return True


def test_valid_anagram():
    """Test cases for Valid Anagram"""
    solution = Solution()

    # Test case 1: Valid anagram
    s1, t1 = "anagram", "nagaram"
    assert solution.isAnagram(s1, t1) == True
    assert solution.isAnagramSort(s1, t1) == True
    assert solution.isAnagramCounter(s1, t1) == True
    assert solution.isAnagramArray(s1, t1) == True
    assert solution.isAnagramOptimized(s1, t1) == True

    # Test case 2: Not an anagram
    s2, t2 = "rat", "car"
    assert solution.isAnagram(s2, t2) == False
    assert solution.isAnagramSort(s2, t2) == False
    assert solution.isAnagramCounter(s2, t2) == False
    assert solution.isAnagramArray(s2, t2) == False
    assert solution.isAnagramOptimized(s2, t2) == False

    # Test case 3: Different lengths
    s3, t3 = "hello", "world"
    assert solution.isAnagram(s3, t3) == False
    assert solution.isAnagramSort(s3, t3) == False
    assert solution.isAnagramCounter(s3, t3) == False
    assert solution.isAnagramArray(s3, t3) == False
    assert solution.isAnagramOptimized(s3, t3) == False

    # Test case 4: Empty strings
    s4, t4 = "", ""
    assert solution.isAnagram(s4, t4) == True
    assert solution.isAnagramSort(s4, t4) == True
    assert solution.isAnagramCounter(s4, t4) == True
    assert solution.isAnagramArray(s4, t4) == True
    assert solution.isAnagramOptimized(s4, t4) == True

    # Test case 5: Single character
    s5, t5 = "a", "a"
    assert solution.isAnagram(s5, t5) == True
    assert solution.isAnagramSort(s5, t5) == True
    assert solution.isAnagramCounter(s5, t5) == True
    assert solution.isAnagramArray(s5, t5) == True
    assert solution.isAnagramOptimized(s5, t5) == True

    # Test case 6: Same string
    s6, t6 = "hello", "hello"
    assert solution.isAnagram(s6, t6) == True
    assert solution.isAnagramSort(s6, t6) == True
    assert solution.isAnagramCounter(s6, t6) == True
    assert solution.isAnagramArray(s6, t6) == True
    assert solution.isAnagramOptimized(s6, t6) == True

    # Test case 7: Repeated characters
    s7, t7 = "aacc", "ccac"
    assert solution.isAnagram(s7, t7) == False
    assert solution.isAnagramSort(s7, t7) == False
    assert solution.isAnagramCounter(s7, t7) == False
    assert solution.isAnagramArray(s7, t7) == False
    assert solution.isAnagramOptimized(s7, t7) == False

    print("All test cases passed!")


if __name__ == "__main__":
    test_valid_anagram()
