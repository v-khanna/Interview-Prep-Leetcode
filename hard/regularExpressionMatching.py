class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D DP table
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle patterns with *
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]  # Zero occurrence
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[len(s)][len(p)]


# Alternative solution using recursion with memoization
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and p[j] in {s[i], "."}

                if j + 1 < len(p) and p[j + 1] == "*":
                    ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
                else:
                    ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    # Test cases
    test_cases = [
        ("aa", "a"),  # False
        ("aa", "a*"),  # True
        ("ab", ".*"),  # True
        ("aab", "c*a*b"),  # True
        ("mississippi", "mis*is*p*."),  # False
        ("", ".*"),  # True
        ("a", ".*..a*"),  # False
    ]

    for s, p in test_cases:
        result1 = solution.isMatch(s, p)
        result2 = solution2.isMatch(s, p)
        print(f"'{s}' matches '{p}': {result1} (DP), {result2} (recursion)")
