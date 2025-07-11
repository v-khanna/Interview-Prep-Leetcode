"""
Burst Balloons (Hard)
https://leetcode.com/problems/burst-balloons/

Problem: Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it.
Find the maximum coins you can collect by bursting the balloons wisely.

Example:
Input: [3,1,5,8]
Output: 167 (Burst 1, then 5, then 3, then 8)

Approach: Dynamic Programming with memoization
Time Complexity: O(n³)
Space Complexity: O(n²)
"""


class Solution:
    def maxCoins(self, nums):
        """
        Find maximum coins using dynamic programming
        """
        # Add virtual balloons at the beginning and end
        balloons = [1] + nums + [1]
        n = len(balloons)

        # dp[i][j] = max coins from bursting balloons i+1 to j-1
        dp = [[0] * n for _ in range(n)]

        # Fill dp table diagonally
        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                # Try each balloon as the last one to burst
                for k in range(left + 1, right):
                    coins = balloons[left] * balloons[k] * balloons[right]
                    coins += dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]

    def maxCoinsMemoization(self, nums):
        """
        Alternative approach using memoization
        """
        # Add virtual balloons
        balloons = [1] + nums + [1]
        n = len(balloons)

        # Memoization cache
        memo = {}

        def dp(left, right):
            if left + 1 == right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            max_coins = 0

            # Try each balloon as the last one to burst
            for k in range(left + 1, right):
                coins = balloons[left] * balloons[k] * balloons[right]
                coins += dp(left, k) + dp(k, right)
                max_coins = max(max_coins, coins)

            memo[(left, right)] = max_coins
            return max_coins

        return dp(0, n - 1)

    def maxCoinsOptimized(self, nums):
        """
        Optimized approach with better space usage
        """
        if not nums:
            return 0

        # Add virtual balloons
        balloons = [1] + nums + [1]
        n = len(balloons)

        # dp[i][j] = max coins from bursting balloons i+1 to j-1
        dp = [[0] * n for _ in range(n)]

        # Fill dp table from bottom to top, left to right
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                # Try each balloon as the last one to burst
                for k in range(i + 1, j):
                    coins = balloons[i] * balloons[k] * balloons[j]
                    coins += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], coins)

        return dp[0][n - 1]

    def maxCoinsRecursive(self, nums):
        """
        Recursive approach with memoization (most intuitive)
        """
        if not nums:
            return 0

        # Add virtual balloons
        balloons = [1] + nums + [1]
        n = len(balloons)

        # Memoization cache
        memo = {}

        def burst(left, right):
            # Base case: no balloons to burst
            if left + 1 >= right:
                return 0

            # Check memoization cache
            if (left, right) in memo:
                return memo[(left, right)]

            max_coins = 0

            # Try bursting each balloon as the last one
            for i in range(left + 1, right):
                # Coins from bursting balloon i
                coins = balloons[left] * balloons[i] * balloons[right]
                # Add coins from left and right subproblems
                coins += burst(left, i) + burst(i, right)
                max_coins = max(max_coins, coins)

            memo[(left, right)] = max_coins
            return max_coins

        return burst(0, n - 1)


def test_burst_balloons():
    """Test cases for Burst Balloons"""
    solution = Solution()

    # Test case 1: Basic case
    nums1 = [3, 1, 5, 8]
    assert solution.maxCoins(nums1) == 167
    assert solution.maxCoinsMemoization(nums1) == 167
    assert solution.maxCoinsOptimized(nums1) == 167
    assert solution.maxCoinsRecursive(nums1) == 167

    # Test case 2: Single balloon
    nums2 = [5]
    assert solution.maxCoins(nums2) == 5
    assert solution.maxCoinsMemoization(nums2) == 5
    assert solution.maxCoinsOptimized(nums2) == 5
    assert solution.maxCoinsRecursive(nums2) == 5

    # Test case 3: Two balloons
    nums3 = [3, 4]
    assert solution.maxCoins(nums3) == 12
    assert solution.maxCoinsMemoization(nums3) == 12
    assert solution.maxCoinsOptimized(nums3) == 12
    assert solution.maxCoinsRecursive(nums3) == 12

    # Test case 4: Empty array
    nums4 = []
    assert solution.maxCoins(nums4) == 0
    assert solution.maxCoinsMemoization(nums4) == 0
    assert solution.maxCoinsOptimized(nums4) == 0
    assert solution.maxCoinsRecursive(nums4) == 0

    # Test case 5: All same values
    nums5 = [2, 2, 2]
    assert solution.maxCoins(nums5) == 8
    assert solution.maxCoinsMemoization(nums5) == 8
    assert solution.maxCoinsOptimized(nums5) == 8
    assert solution.maxCoinsRecursive(nums5) == 8

    print("All test cases passed!")


if __name__ == "__main__":
    test_burst_balloons()
