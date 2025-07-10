"""
LeetCode 70: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45
"""

def climbStairs(n: int) -> int:
    """
    Dynamic Programming approach - Fibonacci sequence
    dp[i] = dp[i-1] + dp[i-2]
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 2:
        return n
    
    # Only need to store last two values
    prev2 = 1  # dp[0]
    prev1 = 2  # dp[1]
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

def climbStairsDP(n: int) -> int:
    """
    Dynamic Programming approach with array
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def climbStairsRecursive(n: int) -> int:
    """
    Recursive approach with memoization
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    memo = {}
    
    def helper(n):
        if n in memo:
            return memo[n]
        if n <= 2:
            return n
        memo[n] = helper(n-1) + helper(n-2)
        return memo[n]
    
    return helper(n)

# Test cases
def test_climbStairs():
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
        (20, 10946)
    ]
    
    for n, expected in test_cases:
        result1 = climbStairs(n)
        result2 = climbStairsDP(n)
        result3 = climbStairsRecursive(n)
        assert result1 == expected, f"climbStairs({n}) = {result1}, expected {expected}"
        assert result2 == expected, f"climbStairsDP({n}) = {result2}, expected {expected}"
        assert result3 == expected, f"climbStairsRecursive({n}) = {result3}, expected {expected}"
        print(f"✓ n = {n}: {result1} ways")

if __name__ == "__main__":
    test_climbStairs()
    print("All test cases passed!")