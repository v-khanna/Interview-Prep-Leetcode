"""
Remove Invalid Parentheses (Hard)
https://leetcode.com/problems/remove-invalid-parentheses/

Problem: Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid. Return all possible results.

Example:
Input: s = "()())()"
Output: ["(())()","()()()"]

Approach: BFS with pruning
Time Complexity: O(2^n)
Space Complexity: O(n)
"""


class Solution:
    def removeInvalidParentheses(self, s):
        """
        Remove invalid parentheses using BFS
        """
        if not s:
            return [""]

        def isValid(s):
            """Check if string has valid parentheses"""
            count = 0
            for char in s:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def getInvalidCount(s):
            """Get number of invalid parentheses"""
            left = right = 0
            for char in s:
                if char == "(":
                    left += 1
                elif char == ")":
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            return left, right

        # Get minimum removals needed
        left_remove, right_remove = getInvalidCount(s)

        # BFS to find all valid strings
        queue = [s]
        visited = {s}
        result = []
        found = False

        while queue and not found:
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.pop(0)

                if isValid(curr):
                    result.append(curr)
                    found = True

                if found:
                    continue

                # Try removing each character
                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue

                    # Skip duplicates
                    if i > 0 and curr[i] == curr[i - 1]:
                        continue

                    # Skip if removing this char won't help
                    if curr[i] == "(" and left_remove == 0:
                        continue
                    if curr[i] == ")" and right_remove == 0:
                        continue

                    new_str = curr[:i] + curr[i + 1 :]
                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append(new_str)

        return result if result else [""]

    def removeInvalidParenthesesOptimized(self, s):
        """
        Optimized version with better pruning
        """
        if not s:
            return [""]

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

        def getMinRemovals(s):
            """Calculate minimum removals needed"""
            left = right = 0
            for char in s:
                if char == "(":
                    left += 1
                elif char == ")":
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            return left, right

        left_remove, right_remove = getMinRemovals(s)

        # BFS with level tracking
        queue = [(s, 0, 0, 0)]  # (string, index, left_count, right_count)
        visited = set()
        result = []
        min_len = len(s) - left_remove - right_remove

        while queue:
            curr, i, left, right = queue.pop(0)

            if len(curr) == min_len:
                if isValid(curr):
                    result.append(curr)
                continue

            if i >= len(curr):
                continue

            char = curr[i]

            # Skip non-parentheses
            if char not in "()":
                queue.append((curr, i + 1, left, right))
                continue

            # Try keeping the character
            if char == "(":
                queue.append((curr, i + 1, left + 1, right))
            elif char == ")" and left > right:
                queue.append((curr, i + 1, left, right + 1))

            # Try removing the character
            new_str = curr[:i] + curr[i + 1 :]
            if new_str not in visited:
                visited.add(new_str)
                queue.append((new_str, i, left, right))

        return result if result else [""]

    def removeInvalidParenthesesDFS(self, s):
        """
        DFS approach with pruning
        """
        if not s:
            return [""]

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

        def getMinRemovals(s):
            left = right = 0
            for char in s:
                if char == "(":
                    left += 1
                elif char == ")":
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            return left, right

        left_remove, right_remove = getMinRemovals(s)
        result = set()

        def dfs(s, index, left_count, right_count, left_removed, right_removed):
            if index == len(s):
                if (
                    left_count == right_count
                    and left_removed == left_remove
                    and right_removed == right_remove
                ):
                    result.add(s)
                return

            char = s[index]

            if char == "(":
                # Keep the '('
                dfs(
                    s,
                    index + 1,
                    left_count + 1,
                    right_count,
                    left_removed,
                    right_removed,
                )
                # Remove the '('
                if left_removed < left_remove:
                    dfs(
                        s[:index] + s[index + 1 :],
                        index,
                        left_count,
                        right_count,
                        left_removed + 1,
                        right_removed,
                    )
            elif char == ")":
                # Keep the ')'
                if left_count > right_count:
                    dfs(
                        s,
                        index + 1,
                        left_count,
                        right_count + 1,
                        left_removed,
                        right_removed,
                    )
                # Remove the ')'
                if right_removed < right_remove:
                    dfs(
                        s[:index] + s[index + 1 :],
                        index,
                        left_count,
                        right_count,
                        left_removed,
                        right_removed + 1,
                    )
            else:
                # Keep non-parentheses
                dfs(s, index + 1, left_count, right_count, left_removed, right_removed)

        dfs(s, 0, 0, 0, 0, 0)
        return list(result) if result else [""]

    def removeInvalidParenthesesGreedy(self, s):
        """
        Greedy approach with two passes
        """
        if not s:
            return [""]

        def removeInvalid(s, open_char, close_char):
            """Remove invalid parentheses in one direction"""
            count = 0
            result = []

            for char in s:
                if char == open_char:
                    count += 1
                elif char == close_char:
                    count -= 1

                if count >= 0:
                    result.append(char)
                else:
                    count = 0

            return "".join(result)

        # Remove invalid ')' from left to right
        s1 = removeInvalid(s, "(", ")")
        # Remove invalid '(' from right to left
        s2 = removeInvalid(s1[::-1], ")", "(")[::-1]

        # Check if result is valid
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

        if isValid(s2):
            return [s2]
        else:
            return [""]


def test_remove_invalid_parentheses():
    """Test cases for Remove Invalid Parentheses"""
    solution = Solution()

    # Test case 1: Basic case
    s1 = "()())()"
    result1 = solution.removeInvalidParentheses(s1)
    expected1 = ["(())()", "()()()"]
    assert sorted(result1) == sorted(expected1)

    result1_opt = solution.removeInvalidParenthesesOptimized(s1)
    assert sorted(result1_opt) == sorted(expected1)

    result1_dfs = solution.removeInvalidParenthesesDFS(s1)
    assert sorted(result1_dfs) == sorted(expected1)

    result1_greedy = solution.removeInvalidParenthesesGreedy(s1)
    assert sorted(result1_greedy) == sorted(expected1)

    # Test case 2: Single invalid parenthesis
    s2 = "(a)())()"
    result2 = solution.removeInvalidParentheses(s2)
    expected2 = ["(a())()", "(a)()()"]
    assert sorted(result2) == sorted(expected2)

    # Test case 3: All invalid
    s3 = ")("
    result3 = solution.removeInvalidParentheses(s3)
    assert result3 == [""]

    # Test case 4: Already valid
    s4 = "()"
    result4 = solution.removeInvalidParentheses(s4)
    assert result4 == ["()"]

    # Test case 5: Empty string
    s5 = ""
    result5 = solution.removeInvalidParentheses(s5)
    assert result5 == [""]

    # Test case 6: No parentheses
    s6 = "abc"
    result6 = solution.removeInvalidParentheses(s6)
    assert result6 == ["abc"]

    print("All test cases passed!")


if __name__ == "__main__":
    test_remove_invalid_parentheses()
