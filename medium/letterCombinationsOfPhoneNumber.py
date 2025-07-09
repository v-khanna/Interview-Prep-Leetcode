"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for char in phone[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.letterCombinations("23")
    )  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
