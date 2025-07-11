"""
Basic Calculator (Hard)
https://leetcode.com/problems/basic-calculator/

Problem: Implement a basic calculator to evaluate a simple expression string.

Example:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Approach: Stack-based evaluation
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def calculate(self, s):
        """
        Evaluate expression with parentheses, +, and - operators
        """
        stack = []
        result = 0
        sign = 1  # 1 for positive, -1 for negative
        i = 0

        while i < len(s):
            char = s[i]

            if char.isdigit():
                # Extract the complete number
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
                i -= 1  # Adjust for the increment in the main loop

            elif char == "+":
                sign = 1

            elif char == "-":
                sign = -1

            elif char == "(":
                # Push current result and sign onto stack
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif char == ")":
                # Pop sign and previous result from stack
                result *= stack.pop()  # sign
                result += stack.pop()  # previous result

            i += 1

        return result

    def calculateWithSpaces(self, s):
        """
        Alternative approach that handles spaces more explicitly
        """

        def evaluate(tokens):
            stack = []
            i = 0

            while i < len(tokens):
                token = tokens[i]

                if token == "(":
                    stack.append(token)
                elif token == ")":
                    # Evaluate until we find matching '('
                    temp_stack = []
                    while stack and stack[-1] != "(":
                        temp_stack.append(stack.pop())
                    stack.pop()  # Remove '('

                    # Evaluate the expression in parentheses
                    result = evaluate_expression(temp_stack[::-1])
                    stack.append(result)
                else:
                    stack.append(token)
                i += 1

            return evaluate_expression(stack)

        def evaluate_expression(tokens):
            if not tokens:
                return 0

            result = int(tokens[0])
            i = 1

            while i < len(tokens):
                if tokens[i] == "+":
                    result += int(tokens[i + 1])
                elif tokens[i] == "-":
                    result -= int(tokens[i + 1])
                i += 2

            return result

        # Tokenize the string
        tokens = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i] in "()+-":
                tokens.append(s[i])
                i += 1
            elif s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                tokens.append(str(num))
            else:
                i += 1

        return evaluate(tokens)


def test_basic_calculator():
    """Test cases for Basic Calculator"""
    solution = Solution()

    # Test case 1: Basic expression
    assert solution.calculate("1 + 1") == 2
    assert solution.calculateWithSpaces("1 + 1") == 2

    # Test case 2: Expression with parentheses
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert solution.calculateWithSpaces("(1+(4+5+2)-3)+(6+8)") == 23

    # Test case 3: Simple subtraction
    assert solution.calculate("2-1 + 2") == 3
    assert solution.calculateWithSpaces("2-1 + 2") == 3

    # Test case 4: Nested parentheses
    assert solution.calculate("1-(5)") == -4
    assert solution.calculateWithSpaces("1-(5)") == -4

    # Test case 5: Complex nested expression
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert solution.calculateWithSpaces("(1+(4+5+2)-3)+(6+8)") == 23

    # Test case 6: Single number
    assert solution.calculate("123") == 123
    assert solution.calculateWithSpaces("123") == 123

    print("All test cases passed!")


if __name__ == "__main__":
    test_basic_calculator()
