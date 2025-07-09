class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack or stack.pop() != brackets[char]:
                    return False

        return len(stack) == 0


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "()"
    print(f"'{s1}' is valid: {solution.isValid(s1)}")  # True

    # Test case 2
    s2 = "()[]{}"
    print(f"'{s2}' is valid: {solution.isValid(s2)}")  # True

    # Test case 3
    s3 = "(]"
    print(f"'{s3}' is valid: {solution.isValid(s3)}")  # False

    # Test case 4
    s4 = "([)]"
    print(f"'{s4}' is valid: {solution.isValid(s4)}")  # False
