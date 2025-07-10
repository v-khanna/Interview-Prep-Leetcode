"""
LeetCode 1143: Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) 
deleted without changing the relative order of the remaining characters.

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
"""

def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    2D Dynamic Programming approach
    
    dp[i][j] = LCS of text1[0:i] and text2[0:j]
    
    If text1[i-1] == text2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
    Else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(text1), len(text2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def longestCommonSubsequenceOptimized(text1: str, text2: str) -> int:
    """
    Space optimized version using only two rows
    
    Time Complexity: O(m * n)
    Space Complexity: O(min(m, n))
    """
    # Make sure text1 is the shorter string
    if len(text1) > len(text2):
        text1, text2 = text2, text1
    
    m, n = len(text1), len(text2)
    
    # Only need previous and current row
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text2[i-1] == text1[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr, prev
    
    return prev[m]

def longestCommonSubsequenceWithString(text1: str, text2: str) -> tuple[int, str]:
    """
    Returns both length and actual LCS string
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(text1), len(text2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct LCS string
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return dp[m][n], ''.join(reversed(lcs))

def longestCommonSubsequenceRecursive(text1: str, text2: str) -> int:
    """
    Recursive approach with memoization
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    memo = {}
    
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if text1[i-1] == text2[j-1]:
            result = 1 + helper(i-1, j-1)
        else:
            result = max(helper(i-1, j), helper(i, j-1))
        
        memo[(i, j)] = result
        return result
    
    return helper(len(text1), len(text2))

def printLCSTable(text1: str, text2: str):
    """
    Utility function to visualize the DP table
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Print table
    print(f"\nDP table for '{text1}' and '{text2}':")
    print("    ", end="")
    print("".join(f"{c:3}" for c in " " + text2))
    for i in range(m + 1):
        char = " " if i == 0 else text1[i-1]
        print(f"{char:2} ", end="")
        for j in range(n + 1):
            print(f"{dp[i][j]:3}", end="")
        print()

# Test cases
def test_lcs():
    test_cases = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "abc", 0),
        ("abc", "", 0),
        ("a", "a", 1),
        ("abcdgh", "aedfhr", 3),
        ("aggtab", "gxtxayb", 4),
        ("programming", "grading", 6),
        ("ABCDGH", "AEDFHR", 3)
    ]
    
    for text1, text2, expected in test_cases:
        result1 = longestCommonSubsequence(text1, text2)
        result2 = longestCommonSubsequenceOptimized(text1, text2)
        result3 = longestCommonSubsequenceRecursive(text1, text2)
        length, lcs_str = longestCommonSubsequenceWithString(text1, text2)
        
        assert result1 == expected, f"LCS('{text1}', '{text2}') = {result1}, expected {expected}"
        assert result2 == expected, f"LCS optimized('{text1}', '{text2}') = {result2}, expected {expected}"
        assert result3 == expected, f"LCS recursive('{text1}', '{text2}') = {result3}, expected {expected}"
        assert length == expected, f"LCS with string('{text1}', '{text2}') = {length}, expected {expected}"
        
        print(f"✓ '{text1}' & '{text2}': LCS length = {result1}, LCS = '{lcs_str}'")

if __name__ == "__main__":
    test_lcs()
    print("\nAll test cases passed!")
    
    # Demonstrate DP table visualization
    printLCSTable("abcde", "ace")