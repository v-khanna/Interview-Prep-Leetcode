"""
Basic Calculator II (Hard)
https://leetcode.com/problems/basic-calculator-ii/

Problem: Implement a basic calculator to evaluate a simple expression string with +, -, *, / operators.

Example:
Input: "3+2*2"
Output: 7

Approach: Stack-based evaluation with precedence handling
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def calculate(self, s):
        """
        Evaluate expression with +, -, *, / operators (no parentheses)
        """
        stack = []
        num = 0
        sign = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if (not char.isdigit() and char != " ") or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    # Integer division (truncate toward zero)
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(abs(prev) // num))
                    else:
                        stack.append(prev // num)

                sign = char
                num = 0

        return sum(stack)

    def calculateOptimized(self, s):
        """
        Optimized approach without stack - process multiplication/division immediately
        """
        result = 0
        curr = 0
        prev = 0
        sign = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                curr = curr * 10 + int(char)

            if (not char.isdigit() and char != " ") or i == len(s) - 1:
                if sign == "+":
                    result += prev
                    prev = curr
                elif sign == "-":
                    result += prev
                    prev = -curr
                elif sign == "*":
                    prev *= curr
                elif sign == "/":
                    # Integer division (truncate toward zero)
                    if prev < 0:
                        prev = -(abs(prev) // curr)
                    else:
                        prev = prev // curr

                sign = char
                curr = 0

        return result + prev

    def calculateWithSpaces(self, s):
        """
        Alternative approach that handles spaces more explicitly
        """

        def tokenize(s):
            tokens = []
            i = 0
            while i < len(s):
                if s[i] == " ":
                    i += 1
                    continue
                elif s[i] in "+-*/":
                    tokens.append(s[i])
                    i += 1
                elif s[i].isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    tokens.append(num)
                else:
                    i += 1
            return tokens

        tokens = tokenize(s)
        if not tokens:
            return 0

        # First pass: handle multiplication and division
        i = 1
        while i < len(tokens) - 1:
            if tokens[i] == "*":
                tokens[i - 1] = tokens[i - 1] * tokens[i + 1]
                tokens.pop(i)
                tokens.pop(i)
            elif tokens[i] == "/":
                # Integer division
                if tokens[i - 1] < 0:
                    tokens[i - 1] = -(abs(tokens[i - 1]) // tokens[i + 1])
                else:
                    tokens[i - 1] = tokens[i - 1] // tokens[i + 1]
                tokens.pop(i)
                tokens.pop(i)
            else:
                i += 2

        # Second pass: handle addition and subtraction
        result = tokens[0]
        i = 1
        while i < len(tokens):
            if tokens[i] == "+":
                result += tokens[i + 1]
            elif tokens[i] == "-":
                result -= tokens[i + 1]
            i += 2

        return result


def test_basic_calculator_ii():
    """Test cases for Basic Calculator II"""
    solution = Solution()

    # Test case 1: Basic multiplication
    assert solution.calculate("3+2*2") == 7
    assert solution.calculateOptimized("3+2*2") == 7
    assert solution.calculateWithSpaces("3+2*2") == 7

    # Test case 2: Division
    assert solution.calculate("3/2") == 1
    assert solution.calculateOptimized("3/2") == 1
    assert solution.calculateWithSpaces("3/2") == 1

    # Test case 3: Complex expression
    assert solution.calculate("3+2*2+1") == 8
    assert solution.calculateOptimized("3+2*2+1") == 8
    assert solution.calculateWithSpaces("3+2*2+1") == 8

    # Test case 4: Division with negative numbers
    assert solution.calculate("14-3/2") == 13
    assert solution.calculateOptimized("14-3/2") == 13
    assert solution.calculateWithSpaces("14-3/2") == 13

    # Test case 5: Multiple operations
    assert solution.calculate("1+2*3-4/2") == 5
    assert solution.calculateOptimized("1+2*3-4/2") == 5
    assert solution.calculateWithSpaces("1+2*3-4/2") == 5

    # Test case 6: Single number
    assert solution.calculate("42") == 42
    assert solution.calculateOptimized("42") == 42
    assert solution.calculateWithSpaces("42") == 42

    print("All test cases passed!")


if __name__ == "__main__":
    test_basic_calculator_ii()
