"""
Word Break II (Hard)
https://leetcode.com/problems/word-break-ii/

Problem: Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Example:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Approach: Backtracking with memoization
Time Complexity: O(n^3 + 2^n)
Space Complexity: O(2^n)
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        Find all possible word break combinations
        """
        wordSet = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sentence in backtrack(end):
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return backtrack(0)

    def wordBreakOptimized(self, s, wordDict):
        """
        Optimized version with early pruning
        """
        wordSet = set(wordDict)
        memo = {}

        def canBreak(s):
            """Check if string can be broken"""
            n = len(s)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and s[j:i] in wordSet:
                        dp[i] = True
                        break

            return dp[n]

        def backtrack(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    # Check if remaining string can be broken
                    remaining = s[end:]
                    if not remaining or canBreak(remaining):
                        for sentence in backtrack(end):
                            if sentence:
                                result.append(word + " " + sentence)
                            else:
                                result.append(word)

            memo[start] = result
            return result

        return backtrack(0)

    def wordBreakDP(self, s, wordDict):
        """
        Dynamic programming approach
        """
        wordSet = set(wordDict)
        n = len(s)

        # dp[i] stores all possible sentences ending at index i
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                word = s[j:i]
                if word in wordSet and dp[j]:
                    for sentence in dp[j]:
                        if sentence:
                            dp[i].append(sentence + " " + word)
                        else:
                            dp[i].append(word)

        return dp[n]

    def wordBreakBacktrack(self, s, wordDict):
        """
        Pure backtracking approach
        """
        wordSet = set(wordDict)
        result = []

        def backtrack(start, path):
            if start == len(s):
                result.append(" ".join(path))
                return

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    path.append(word)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result


def test_word_break_ii():
    """Test cases for Word Break II"""
    solution = Solution()

    # Test case 1: Basic case
    s1 = "catsanddog"
    wordDict1 = ["cat", "cats", "and", "sand", "dog"]
    result1 = solution.wordBreak(s1, wordDict1)
    expected1 = ["cats and dog", "cat sand dog"]
    assert sorted(result1) == sorted(expected1)

    result1_opt = solution.wordBreakOptimized(s1, wordDict1)
    assert sorted(result1_opt) == sorted(expected1)

    result1_dp = solution.wordBreakDP(s1, wordDict1)
    assert sorted(result1_dp) == sorted(expected1)

    result1_bt = solution.wordBreakBacktrack(s1, wordDict1)
    assert sorted(result1_bt) == sorted(expected1)

    # Test case 2: Single word
    s2 = "dog"
    wordDict2 = ["dog"]
    result2 = solution.wordBreak(s2, wordDict2)
    assert result2 == ["dog"]

    # Test case 3: No valid break
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    result3 = solution.wordBreak(s3, wordDict3)
    assert result3 == []

    # Test case 4: Multiple valid breaks
    s4 = "pineapplepenapple"
    wordDict4 = ["apple", "pen", "applepen", "pine", "pineapple"]
    result4 = solution.wordBreak(s4, wordDict4)
    expected4 = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    assert sorted(result4) == sorted(expected4)

    # Test case 5: Empty string
    s5 = ""
    wordDict5 = ["a"]
    result5 = solution.wordBreak(s5, wordDict5)
    assert result5 == [""]

    print("All test cases passed!")


if __name__ == "__main__":
    test_word_break_ii()
