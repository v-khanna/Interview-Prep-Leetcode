"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
"""

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for char in s:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def dfs(
            s, start, left_removed, right_removed, left_count, right_count, path, result
        ):
            if start == len(s):
                if left_removed == 0 and right_removed == 0 and isValid(path):
                    result.add(path)
                return

            char = s[start]

            if char == "(" and left_removed > 0:
                dfs(
                    s,
                    start + 1,
                    left_removed - 1,
                    right_removed,
                    left_count,
                    right_count,
                    path,
                    result,
                )
            elif char == ")" and right_removed > 0:
                dfs(
                    s,
                    start + 1,
                    left_removed,
                    right_removed - 1,
                    left_count,
                    right_count,
                    path,
                    result,
                )

            if char != "(" and char != ")":
                dfs(
                    s,
                    start + 1,
                    left_removed,
                    right_removed,
                    left_count,
                    right_count,
                    path + char,
                    result,
                )
            elif char == "(":
                dfs(
                    s,
                    start + 1,
                    left_removed,
                    right_removed,
                    left_count + 1,
                    right_count,
                    path + char,
                    result,
                )
            elif char == ")" and left_count > right_count:
                dfs(
                    s,
                    start + 1,
                    left_removed,
                    right_removed,
                    left_count,
                    right_count + 1,
                    path + char,
                    result,
                )

        # Count minimum removals needed
        left_removed = right_removed = 0
        for char in s:
            if char == "(":
                left_removed += 1
            elif char == ")":
                if left_removed == 0:
                    right_removed += 1
                else:
                    left_removed -= 1

        result = set()
        dfs(s, 0, left_removed, right_removed, 0, 0, "", result)
        return list(result)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeInvalidParentheses("()())()"))  # ["()()()", "(())()"]
    print(solution.removeInvalidParentheses("(a)())()"))  # ["(a)()()", "(a())()"]
    print(solution.removeInvalidParentheses(")("))  # [""]
