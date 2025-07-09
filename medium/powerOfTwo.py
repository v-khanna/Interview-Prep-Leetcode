"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPowerOfTwo(1))  # Output: True
    print(solution.isPowerOfTwo(16))  # Output: True
    print(solution.isPowerOfTwo(3))  # Output: False
    print(solution.isPowerOfTwo(0))  # Output: False
