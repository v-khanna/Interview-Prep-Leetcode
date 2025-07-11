"""
Integer to English Words (Hard)
https://leetcode.com/problems/integer-to-english-words/

Problem: Convert a non-negative integer num to its English words representation.

Example:
Input: num = 123
Output: "One Hundred Twenty Three"

Approach: Recursive with lookup tables
Time Complexity: O(log n)
Space Complexity: O(log n)
"""


class Solution:
    def numberToWords(self, num):
        """
        Convert integer to English words
        """
        if num == 0:
            return "Zero"

        # Lookup tables
        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        teens = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def convert_less_than_one_thousand(n):
            if n == 0:
                return ""
            elif n < 10:
                return ones[n]
            elif n < 20:
                return teens[n - 10]
            elif n < 100:
                return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
            else:
                return (
                    ones[n // 100]
                    + " Hundred"
                    + (
                        " " + convert_less_than_one_thousand(n % 100)
                        if n % 100 != 0
                        else ""
                    )
                )

        result = ""
        i = 0

        while num > 0:
            if num % 1000 != 0:
                result = (
                    convert_less_than_one_thousand(num % 1000)
                    + (" " + thousands[i] if i > 0 else "")
                    + (" " + result if result else "")
                )
            num //= 1000
            i += 1

        return result.strip()

    def numberToWordsRecursive(self, num):
        """
        Recursive approach
        """
        if num == 0:
            return "Zero"

        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        teens = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        def convert(n):
            if n == 0:
                return ""
            elif n < 10:
                return ones[n]
            elif n < 20:
                return teens[n - 10]
            elif n < 100:
                return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
            elif n < 1000:
                return (
                    ones[n // 100]
                    + " Hundred"
                    + (" " + convert(n % 100) if n % 100 != 0 else "")
                )
            elif n < 1000000:
                return (
                    convert(n // 1000)
                    + " Thousand"
                    + (" " + convert(n % 1000) if n % 1000 != 0 else "")
                )
            elif n < 1000000000:
                return (
                    convert(n // 1000000)
                    + " Million"
                    + (" " + convert(n % 1000000) if n % 1000000 != 0 else "")
                )
            else:
                return (
                    convert(n // 1000000000)
                    + " Billion"
                    + (" " + convert(n % 1000000000) if n % 1000000000 != 0 else "")
                )

        return convert(num)

    def numberToWordsOptimized(self, num):
        """
        Optimized version with better string handling
        """
        if num == 0:
            return "Zero"

        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        teens = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def convert_less_than_one_thousand(n):
            if n == 0:
                return ""
            elif n < 10:
                return ones[n]
            elif n < 20:
                return teens[n - 10]
            elif n < 100:
                return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
            else:
                hundred_part = ones[n // 100] + " Hundred"
                remainder = convert_less_than_one_thousand(n % 100)
                return hundred_part + (" " + remainder if remainder else "")

        result = []
        i = 0

        while num > 0:
            if num % 1000 != 0:
                part = convert_less_than_one_thousand(num % 1000)
                if i > 0:
                    part += " " + thousands[i]
                result.insert(0, part)
            num //= 1000
            i += 1

        return " ".join(result)

    def numberToWordsWithValidation(self, num):
        """
        Version with input validation
        """
        if not isinstance(num, int):
            raise ValueError("Input must be an integer")

        if num < 0:
            raise ValueError("Input must be non-negative")

        if num > 2**31 - 1:
            raise ValueError("Input too large")

        return self.numberToWords(num)


def test_integer_to_english_words():
    """Test cases for Integer to English Words"""
    solution = Solution()

    # Test case 1: Basic cases
    assert solution.numberToWords(123) == "One Hundred Twenty Three"
    assert solution.numberToWordsRecursive(123) == "One Hundred Twenty Three"
    assert solution.numberToWordsOptimized(123) == "One Hundred Twenty Three"

    # Test case 2: Zero
    assert solution.numberToWords(0) == "Zero"
    assert solution.numberToWordsRecursive(0) == "Zero"
    assert solution.numberToWordsOptimized(0) == "Zero"

    # Test case 3: Single digit
    assert solution.numberToWords(5) == "Five"
    assert solution.numberToWordsRecursive(5) == "Five"
    assert solution.numberToWordsOptimized(5) == "Five"

    # Test case 4: Teens
    assert solution.numberToWords(15) == "Fifteen"
    assert solution.numberToWordsRecursive(15) == "Fifteen"
    assert solution.numberToWordsOptimized(15) == "Fifteen"

    # Test case 5: Tens
    assert solution.numberToWords(45) == "Forty Five"
    assert solution.numberToWordsRecursive(45) == "Forty Five"
    assert solution.numberToWordsOptimized(45) == "Forty Five"

    # Test case 6: Hundreds
    assert solution.numberToWords(100) == "One Hundred"
    assert solution.numberToWordsRecursive(100) == "One Hundred"
    assert solution.numberToWordsOptimized(100) == "One Hundred"

    # Test case 7: Thousands
    assert solution.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert (
        solution.numberToWordsRecursive(12345)
        == "Twelve Thousand Three Hundred Forty Five"
    )
    assert (
        solution.numberToWordsOptimized(12345)
        == "Twelve Thousand Three Hundred Forty Five"
    )

    # Test case 8: Millions
    assert (
        solution.numberToWords(1234567)
        == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    )
    assert (
        solution.numberToWordsRecursive(1234567)
        == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    )
    assert (
        solution.numberToWordsOptimized(1234567)
        == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    )

    # Test case 9: Billions
    assert (
        solution.numberToWords(1234567891)
        == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    )
    assert (
        solution.numberToWordsRecursive(1234567891)
        == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    )
    assert (
        solution.numberToWordsOptimized(1234567891)
        == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    )

    print("All test cases passed!")


if __name__ == "__main__":
    test_integer_to_english_words()
