"""
Given an m x n board of characters and a list of strings words, return all words on the board.
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        m, n = len(board), len(board[0])

        def dfs(i, j, node):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in node.children:
                return

            char = board[i][j]
            board[i][j] = "#"
            node = node.children[char]

            if node.is_end:
                result.add(node.word)

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + di, j + dj, node)

            board[i][j] = char

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)

        return list(result)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(solution.findWords(board, words))  # Output: ["eat","oath"]
