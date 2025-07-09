class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenating in both orders doesn't give the same result,
        # there's no common divisor
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD of the lengths
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Return the substring of length gcd
        return str1[: gcd(len(str1), len(str2))]


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    str1 = "ABCABC"
    str2 = "ABC"
    print(solution.gcdOfStrings(str1, str2))  # Output: "ABC"

    # Test case 2
    str1 = "ABABAB"
    str2 = "ABAB"
    print(solution.gcdOfStrings(str1, str2))  # Output: "AB"

    # Test case 3
    str1 = "LEET"
    str2 = "CODE"
    print(solution.gcdOfStrings(str1, str2))  # Output: ""
