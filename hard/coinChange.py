"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount.
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))  # Output: 3
    print(solution.coinChange([2], 3))  # Output: -1
    print(solution.coinChange([1], 0))  # Output: 0
