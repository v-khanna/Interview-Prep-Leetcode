class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Convert to string and check if it reads the same forwards and backwards
        return str(x) == str(x)[::-1]


# Alternative solution without converting to string
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Single digit numbers are always palindromes
        if x < 10:
            return True

        # Find the number of digits
        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    # Test cases
    test_cases = [121, -121, 10, 12321, 0]

    for num in test_cases:
        result1 = solution.isPalindrome(num)
        result2 = solution2.isPalindrome(num)
        print(
            f"{num} is palindrome: {result1} (string method), {result2} (math method)"
        )
