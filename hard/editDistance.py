"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You can perform insert, delete, or replace operations. Also reconstruct one optimal path.
"""

from typing import List, Tuple


class Solution:
    def minDistance(self, word1: str, word2: str) -> Tuple[int, List[str]]:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]  # delete  # insert
                    )  # replace
        # Path reconstruction
        ops = []
        i, j = m, n
        while i > 0 or j > 0:
            if i > 0 and j > 0 and word1[i - 1] == word2[j - 1]:
                i -= 1
                j -= 1
            elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
                ops.append(f"Delete '{word1[i-1]}' from word1 at pos {i-1}")
                i -= 1
            elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
                ops.append(f"Insert '{word2[j-1]}' into word1 at pos {i}")
                j -= 1
            else:
                ops.append(
                    f"Replace '{word1[i-1]}' in word1 at pos {i-1} with '{word2[j-1]}'"
                )
                i -= 1
                j -= 1
        return dp[m][n], ops[::-1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    dist, path = solution.minDistance("horse", "ros")
    print(f"Edit distance: {dist}")
    print("Path:")
    for op in path:
        print(op)
    # Output: 3
    # Path: Replace 'h' with 'r', Delete 'r', Delete 'e'
