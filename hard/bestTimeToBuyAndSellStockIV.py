"""
Best Time to Buy and Sell Stock IV (Hard)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Problem: Find the maximum profit you can achieve with at most k transactions.

Example:
Input: k = 2, prices = [2,4,1]
Output: 2

Approach: Dynamic Programming with state machine
Time Complexity: O(n * k)
Space Complexity: O(k)
"""


class Solution:
    def maxProfit(self, k, prices):
        """
        Find maximum profit with at most k transactions using state machine
        """
        if not prices or k == 0:
            return 0

        n = len(prices)

        # If k >= n//2, we can make unlimited transactions
        if k >= n // 2:
            return self.maxProfitUnlimited(prices)

        # State machine: buy1 -> sell1 -> buy2 -> sell2 -> ... -> buyk -> sellk
        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            # Update states in reverse order to avoid using updated values
            for i in range(k, 0, -1):
                sell[i] = max(sell[i], buy[i] + price)  # Sell i-th stock
                buy[i] = max(buy[i], sell[i - 1] - price)  # Buy i-th stock

        return sell[k]

    def maxProfitUnlimited(self, prices):
        """
        Helper function for unlimited transactions
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    def maxProfitDP(self, k, prices):
        """
        Alternative approach using 2D DP array
        """
        if not prices or k == 0:
            return 0

        n = len(prices)

        # If k >= n//2, we can make unlimited transactions
        if k >= n // 2:
            return self.maxProfitUnlimited(prices)

        # dp[i][j] = max profit with i transactions on day j
        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]  # Buy on day 0

            for j in range(1, n):
                # Don't transact on day j
                dp[i][j] = dp[i][j - 1]

                # Sell on day j (buy on some previous day)
                dp[i][j] = max(dp[i][j], prices[j] + max_diff)

                # Update max_diff for next iteration
                max_diff = max(max_diff, dp[i - 1][j - 1] - prices[j])

        return dp[k][n - 1]

    def maxProfitOptimized(self, k, prices):
        """
        Optimized approach with O(k) space
        """
        if not prices or k == 0:
            return 0

        n = len(prices)

        # If k >= n//2, we can make unlimited transactions
        if k >= n // 2:
            return self.maxProfitUnlimited(prices)

        # Track the best profit for each state
        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(k, 0, -1):
                sell[i] = max(sell[i], buy[i] + price)
                buy[i] = max(buy[i], sell[i - 1] - price)

        return sell[k]

    def maxProfitWithFees(self, k, prices, fee=0):
        """
        Extension: with transaction fees
        """
        if not prices or k == 0:
            return 0

        n = len(prices)

        # If k >= n//2, we can make unlimited transactions
        if k >= n // 2:
            return self.maxProfitUnlimitedWithFees(prices, fee)

        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(k, 0, -1):
                sell[i] = max(sell[i], buy[i] + price)
                buy[i] = max(buy[i], sell[i - 1] - price - fee)

        return sell[k]

    def maxProfitUnlimitedWithFees(self, prices, fee):
        """
        Helper function for unlimited transactions with fees
        """
        hold = -prices[0] - fee
        not_hold = 0

        for i in range(1, len(prices)):
            new_hold = max(hold, not_hold - prices[i] - fee)
            new_not_hold = max(not_hold, hold + prices[i])
            hold = new_hold
            not_hold = new_not_hold

        return not_hold


def test_best_time_to_buy_and_sell_stock_iv():
    """Test cases for Best Time to Buy and Sell Stock IV"""
    solution = Solution()

    # Test case 1: Basic case
    k1, prices1 = 2, [2, 4, 1]
    assert solution.maxProfit(k1, prices1) == 2
    assert solution.maxProfitDP(k1, prices1) == 2
    assert solution.maxProfitOptimized(k1, prices1) == 2

    # Test case 2: No transactions possible
    k2, prices2 = 2, [3, 2, 6, 5, 0, 3]
    assert solution.maxProfit(k2, prices2) == 7
    assert solution.maxProfitDP(k2, prices2) == 7
    assert solution.maxProfitOptimized(k2, prices2) == 7

    # Test case 3: Single transaction
    k3, prices3 = 1, [1, 2]
    assert solution.maxProfit(k3, prices3) == 1
    assert solution.maxProfitDP(k3, prices3) == 1
    assert solution.maxProfitOptimized(k3, prices3) == 1

    # Test case 4: No profit possible
    k4, prices4 = 2, [3, 2, 1]
    assert solution.maxProfit(k4, prices4) == 0
    assert solution.maxProfitDP(k4, prices4) == 0
    assert solution.maxProfitOptimized(k4, prices4) == 0

    # Test case 5: Unlimited transactions
    k5, prices5 = 10, [1, 2, 3, 4, 5]
    assert solution.maxProfit(k5, prices5) == 4
    assert solution.maxProfitDP(k5, prices5) == 4
    assert solution.maxProfitOptimized(k5, prices5) == 4

    # Test case 6: Empty prices
    k6, prices6 = 2, []
    assert solution.maxProfit(k6, prices6) == 0
    assert solution.maxProfitDP(k6, prices6) == 0
    assert solution.maxProfitOptimized(k6, prices6) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_best_time_to_buy_and_sell_stock_iv()
