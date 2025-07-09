"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight(11))  # Output: 3 (1011)
    print(solution.hammingWeight(128))  # Output: 1 (10000000)
    print(solution.hammingWeight(4294967293))  # Output: 31
