"""
Best Time to Buy and Sell Stock III (Hard)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Problem: Find the maximum profit you can achieve with at most two transactions.

Example:
Input: [3,3,5,0,0,3,1,4]
Output: 6 (Buy on day 4, sell on day 6, buy on day 7, sell on day 8)

Approach: Dynamic Programming with state machine
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices):
        """
        Find maximum profit with at most 2 transactions using state machine
        """
        if not prices:
            return 0

        # State machine: buy1 -> sell1 -> buy2 -> sell2
        buy1 = float("-inf")  # First buy
        sell1 = 0  # First sell
        buy2 = float("-inf")  # Second buy
        sell2 = 0  # Second sell

        for price in prices:
            # Update states in reverse order to avoid using updated values
            sell2 = max(sell2, buy2 + price)  # Sell second stock
            buy2 = max(buy2, sell1 - price)  # Buy second stock
            sell1 = max(sell1, buy1 + price)  # Sell first stock
            buy1 = max(buy1, -price)  # Buy first stock

        return sell2

    def maxProfitDP(self, prices):
        """
        Alternative approach using 2D DP array
        """
        if not prices:
            return 0

        n = len(prices)
        k = 2  # Maximum number of transactions

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

    def maxProfitOptimized(self, prices):
        """
        Optimized approach with O(1) space
        """
        if not prices:
            return 0

        # Track the best profit for each state
        first_buy = float("-inf")
        first_sell = 0
        second_buy = float("-inf")
        second_sell = 0

        for price in prices:
            # We can either:
            # 1. Not do anything
            # 2. Buy first stock (if we haven't bought yet)
            # 3. Sell first stock (if we have bought)
            # 4. Buy second stock (if we have sold first)
            # 5. Sell second stock (if we have bought second)

            second_sell = max(second_sell, second_buy + price)
            second_buy = max(second_buy, first_sell - price)
            first_sell = max(first_sell, first_buy + price)
            first_buy = max(first_buy, -price)

        return second_sell

    def maxProfitWithFees(self, prices, fee=0):
        """
        Extension: with transaction fees
        """
        if not prices:
            return 0

        hold = -prices[0] - fee  # Cost to buy first stock
        not_hold = 0  # No stock held

        for i in range(1, len(prices)):
            # Either keep holding or buy today
            new_hold = max(hold, not_hold - prices[i] - fee)
            # Either keep not holding or sell today
            new_not_hold = max(not_hold, hold + prices[i])

            hold = new_hold
            not_hold = new_not_hold

        return not_hold


def test_best_time_to_buy_and_sell_stock_iii():
    """Test cases for Best Time to Buy and Sell Stock III"""
    solution = Solution()

    # Test case 1: Basic case
    prices1 = [3, 3, 5, 0, 0, 3, 1, 4]
    assert solution.maxProfit(prices1) == 6
    assert solution.maxProfitDP(prices1) == 6
    assert solution.maxProfitOptimized(prices1) == 6

    # Test case 2: Single transaction is better
    prices2 = [1, 2, 3, 4, 5]
    assert solution.maxProfit(prices2) == 4
    assert solution.maxProfitDP(prices2) == 4
    assert solution.maxProfitOptimized(prices2) == 4

    # Test case 3: No profit possible
    prices3 = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices3) == 0
    assert solution.maxProfitDP(prices3) == 0
    assert solution.maxProfitOptimized(prices3) == 0

    # Test case 4: Two separate profitable transactions
    prices4 = [1, 5, 3, 7, 2, 8]
    assert solution.maxProfit(prices4) == 11
    assert solution.maxProfitDP(prices4) == 11
    assert solution.maxProfitOptimized(prices4) == 11

    # Test case 5: Single price
    prices5 = [1]
    assert solution.maxProfit(prices5) == 0
    assert solution.maxProfitDP(prices5) == 0
    assert solution.maxProfitOptimized(prices5) == 0

    # Test case 6: Empty array
    prices6 = []
    assert solution.maxProfit(prices6) == 0
    assert solution.maxProfitDP(prices6) == 0
    assert solution.maxProfitOptimized(prices6) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_best_time_to_buy_and_sell_stock_iii()
