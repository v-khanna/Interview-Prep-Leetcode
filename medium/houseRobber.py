"""
LeetCode 198: House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""

def rob(nums: list[int]) -> int:
    """
    Dynamic Programming - Space Optimized
    
    For each house, we have two choices:
    1. Rob this house: prev_prev + current_house
    2. Don't rob: prev_max
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev_prev = 0  # max money up to i-2
    prev = 0       # max money up to i-1
    
    for money in nums:
        current = max(prev, prev_prev + money)
        prev_prev = prev
        prev = current
    
    return prev

def robDP(nums: list[int]) -> int:
    """
    Dynamic Programming with array
    
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[n-1]

def robRecursive(nums: list[int]) -> int:
    """
    Recursive approach with memoization
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    memo = {}
    
    def helper(i):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        
        # Choice: rob house i or don't rob house i
        rob_current = nums[i] + helper(i-2)
        dont_rob = helper(i-1)
        
        memo[i] = max(rob_current, dont_rob)
        return memo[i]
    
    return helper(len(nums) - 1)

def robWithPath(nums: list[int]) -> tuple[int, list[int]]:
    """
    Returns both maximum money and which houses to rob
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0, []
    if len(nums) == 1:
        return nums[0], [0]
    
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    # Reconstruct path
    path = []
    i = n - 1
    while i >= 0:
        if i == 0:
            if dp[i] > 0:
                path.append(i)
            break
        elif i == 1:
            if dp[i] == nums[1]:
                path.append(i)
            else:
                path.append(0)
            break
        else:
            if dp[i] == dp[i-1]:
                i -= 1
            else:
                path.append(i)
                i -= 2
    
    return dp[n-1], path[::-1]

# Test cases
def test_rob():
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([5], 5),
        ([1, 2], 2),
        ([2, 1], 2),
        ([1, 3, 1, 3, 100], 103),
        ([2, 7, 9, 3, 1, 5, 6], 18)
    ]
    
    for nums, expected in test_cases:
        result1 = rob(nums)
        result2 = robDP(nums)
        result3 = robRecursive(nums)
        max_money, path = robWithPath(nums)
        
        assert result1 == expected, f"rob({nums}) = {result1}, expected {expected}"
        assert result2 == expected, f"robDP({nums}) = {result2}, expected {expected}"
        assert result3 == expected, f"robRecursive({nums}) = {result3}, expected {expected}"
        assert max_money == expected, f"robWithPath({nums}) = {max_money}, expected {expected}"
        
        houses_money = sum(nums[i] for i in path)
        print(f"✓ nums = {nums}: max money = {result1}, rob houses {path} (total: {houses_money})")

if __name__ == "__main__":
    test_rob()
    print("All test cases passed!")