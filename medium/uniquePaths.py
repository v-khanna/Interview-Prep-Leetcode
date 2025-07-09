"""
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. Return the number of possible unique paths to the bottom-right corner.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(3, 7))  # Output: 28
    print(solution.uniquePaths(3, 2))  # Output: 3
