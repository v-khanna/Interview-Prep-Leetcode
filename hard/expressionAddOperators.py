"""
Expression Add Operators (Hard)
https://leetcode.com/problems/expression-add-operators/

Problem: Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Example:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

Approach: Backtracking with expression evaluation
Time Complexity: O(4^n)
Space Complexity: O(n)
"""


class Solution:
    def addOperators(self, num, target):
        """
        Find all expressions that evaluate to target
        """
        if not num:
            return []

        result = []

        def backtrack(index, path, value, prev):
            """
            Backtrack to find all valid expressions
            index: current position in num
            path: current expression string
            value: current evaluated value
            prev: previous operand for multiplication
            """
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index, len(num)):
                # Skip leading zeros
                if i > index and num[index] == "0":
                    break

                curr_str = num[index : i + 1]
                curr_val = int(curr_str)

                if index == 0:
                    # First number, no operator needed
                    backtrack(i + 1, curr_str, curr_val, curr_val)
                else:
                    # Add '+'
                    backtrack(i + 1, path + "+" + curr_str, value + curr_val, curr_val)

                    # Add '-'
                    backtrack(i + 1, path + "-" + curr_str, value - curr_val, -curr_val)

                    # Add '*'
                    backtrack(
                        i + 1,
                        path + "*" + curr_str,
                        value - prev + prev * curr_val,
                        prev * curr_val,
                    )

        backtrack(0, "", 0, 0)
        return result

    def addOperatorsOptimized(self, num, target):
        """
        Optimized version with early termination
        """
        if not num:
            return []

        result = []

        def backtrack(index, path, value, prev):
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index, len(num)):
                # Skip leading zeros
                if i > index and num[index] == "0":
                    break

                curr_str = num[index : i + 1]
                curr_val = int(curr_str)

                if index == 0:
                    backtrack(i + 1, curr_str, curr_val, curr_val)
                else:
                    # Add '+'
                    backtrack(i + 1, path + "+" + curr_str, value + curr_val, curr_val)

                    # Add '-'
                    backtrack(i + 1, path + "-" + curr_str, value - curr_val, -curr_val)

                    # Add '*'
                    backtrack(
                        i + 1,
                        path + "*" + curr_str,
                        value - prev + prev * curr_val,
                        prev * curr_val,
                    )

        backtrack(0, "", 0, 0)
        return result

    def addOperatorsWithValidation(self, num, target):
        """
        Version with additional validation
        """
        if not num:
            return []

        result = []

        def isValid(num_str):
            """Check if number is valid (no leading zeros)"""
            return len(num_str) == 1 or num_str[0] != "0"

        def backtrack(index, path, value, prev):
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index, len(num)):
                curr_str = num[index : i + 1]

                # Skip invalid numbers (leading zeros)
                if not isValid(curr_str):
                    break

                curr_val = int(curr_str)

                if index == 0:
                    backtrack(i + 1, curr_str, curr_val, curr_val)
                else:
                    # Add '+'
                    backtrack(i + 1, path + "+" + curr_str, value + curr_val, curr_val)

                    # Add '-'
                    backtrack(i + 1, path + "-" + curr_str, value - curr_val, -curr_val)

                    # Add '*'
                    backtrack(
                        i + 1,
                        path + "*" + curr_str,
                        value - prev + prev * curr_val,
                        prev * curr_val,
                    )

        backtrack(0, "", 0, 0)
        return result

    def addOperatorsIterative(self, num, target):
        """
        Iterative approach using stack
        """
        if not num:
            return []

        result = []
        stack = [(0, "", 0, 0)]  # (index, path, value, prev)

        while stack:
            index, path, value, prev = stack.pop()

            if index == len(num):
                if value == target:
                    result.append(path)
                continue

            for i in range(index, len(num)):
                # Skip leading zeros
                if i > index and num[index] == "0":
                    break

                curr_str = num[index : i + 1]
                curr_val = int(curr_str)

                if index == 0:
                    stack.append((i + 1, curr_str, curr_val, curr_val))
                else:
                    # Add '+'
                    stack.append(
                        (i + 1, path + "+" + curr_str, value + curr_val, curr_val)
                    )

                    # Add '-'
                    stack.append(
                        (i + 1, path + "-" + curr_str, value - curr_val, -curr_val)
                    )

                    # Add '*'
                    stack.append(
                        (
                            i + 1,
                            path + "*" + curr_str,
                            value - prev + prev * curr_val,
                            prev * curr_val,
                        )
                    )

        return result


def test_expression_add_operators():
    """Test cases for Expression Add Operators"""
    solution = Solution()

    # Test case 1: Basic case
    num1 = "123"
    target1 = 6
    result1 = solution.addOperators(num1, target1)
    expected1 = ["1*2*3", "1+2+3"]
    assert sorted(result1) == sorted(expected1)

    result1_opt = solution.addOperatorsOptimized(num1, target1)
    assert sorted(result1_opt) == sorted(expected1)

    result1_val = solution.addOperatorsWithValidation(num1, target1)
    assert sorted(result1_val) == sorted(expected1)

    result1_iter = solution.addOperatorsIterative(num1, target1)
    assert sorted(result1_iter) == sorted(expected1)

    # Test case 2: Single digit
    num2 = "5"
    target2 = 5
    result2 = solution.addOperators(num2, target2)
    assert result2 == ["5"]

    # Test case 3: No valid expressions
    num3 = "123"
    target3 = 100
    result3 = solution.addOperators(num3, target3)
    assert result3 == []

    # Test case 4: Leading zeros
    num4 = "105"
    target4 = 5
    result4 = solution.addOperators(num4, target4)
    expected4 = ["1*0+5", "10-5"]
    assert sorted(result4) == sorted(expected4)

    # Test case 5: Multiple operators
    num5 = "232"
    target5 = 8
    result5 = solution.addOperators(num5, target5)
    expected5 = ["2*3+2", "2+3*2"]
    assert sorted(result5) == sorted(expected5)

    # Test case 6: Empty string
    num6 = ""
    target6 = 0
    result6 = solution.addOperators(num6, target6)
    assert result6 == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_expression_add_operators()
