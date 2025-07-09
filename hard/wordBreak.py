"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.wordBreak("leetcode", ["leet", "code"]))  # True
    print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # True
    print(
        solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    )  # False
