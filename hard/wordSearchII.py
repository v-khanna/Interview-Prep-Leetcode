"""
Word Search II (Hard)
https://leetcode.com/problems/word-search-ii/

Problem: Given an m x n board of characters and a list of strings words, return all words on the board.

Example:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Approach: Trie + DFS with backtracking
Time Complexity: O(m * n * 4^L) where L is max word length
Space Complexity: O(k * L) where k is number of words
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""


class Solution:
    def findWords(self, board, words):
        """
        Find all words on the board using Trie and DFS
        """
        if not board or not board[0] or not words:
            return []

        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word

        m, n = len(board), len(board[0])
        result = set()

        def dfs(i, j, node):
            """DFS to find words starting from position (i, j)"""
            char = board[i][j]

            # Check if current path exists in trie
            if char not in node.children:
                return

            node = node.children[char]

            # If we found a word, add it to result
            if node.is_end:
                result.add(node.word)
                # Mark as found to avoid duplicates
                node.is_end = False

            # Mark current cell as visited
            board[i][j] = "#"

            # Explore all 4 directions
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                    dfs(ni, nj, node)

            # Backtrack
            board[i][j] = char

        # Start DFS from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return list(result)

    def findWordsOptimized(self, board, words):
        """
        Optimized version with early termination
        """
        if not board or not board[0] or not words:
            return []

        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word

        m, n = len(board), len(board[0])
        result = set()

        def dfs(i, j, node):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == "#":
                return

            char = board[i][j]
            if char not in node.children:
                return

            node = node.children[char]

            if node.is_end:
                result.add(node.word)
                node.is_end = False

            # Mark as visited
            board[i][j] = "#"

            # Explore neighbors
            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)

            # Backtrack
            board[i][j] = char

        # Start from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return list(result)

    def findWordsWithPruning(self, board, words):
        """
        Version with pruning optimizations
        """
        if not board or not board[0] or not words:
            return []

        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word

        m, n = len(board), len(board[0])
        result = set()

        def dfs(i, j, node):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == "#":
                return

            char = board[i][j]
            if char not in node.children:
                return

            node = node.children[char]

            if node.is_end:
                result.add(node.word)
                node.is_end = False

            # Mark as visited
            board[i][j] = "#"

            # Explore all directions
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                dfs(ni, nj, node)

            # Backtrack
            board[i][j] = char

        # Start from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return list(result)

    def findWordsIterative(self, board, words):
        """
        Iterative approach using stack
        """
        if not board or not board[0] or not words:
            return []

        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word

        m, n = len(board), len(board[0])
        result = set()

        # Stack: (i, j, node, path)
        stack = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    stack.append((i, j, root, [(i, j)]))

        while stack:
            i, j, node, path = stack.pop()

            char = board[i][j]
            if char not in node.children:
                continue

            node = node.children[char]

            if node.is_end:
                result.add(node.word)
                node.is_end = False

            # Mark as visited
            board[i][j] = "#"

            # Add neighbors to stack
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                    stack.append((ni, nj, node, path + [(ni, nj)]))

            # Backtrack
            board[i][j] = char

        return list(result)


def test_word_search_ii():
    """Test cases for Word Search II"""
    solution = Solution()

    # Test case 1: Basic case
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words1 = ["oath", "pea", "eat", "rain"]
    result1 = solution.findWords(board1, words1)
    expected1 = ["eat", "oath"]
    assert sorted(result1) == sorted(expected1)

    result1_opt = solution.findWordsOptimized(board1, words1)
    assert sorted(result1_opt) == sorted(expected1)

    result1_prune = solution.findWordsWithPruning(board1, words1)
    assert sorted(result1_prune) == sorted(expected1)

    result1_iter = solution.findWordsIterative(board1, words1)
    assert sorted(result1_iter) == sorted(expected1)

    # Test case 2: Single word
    board2 = [["a", "b"], ["c", "d"]]
    words2 = ["abcb"]
    result2 = solution.findWords(board2, words2)
    assert result2 == []

    # Test case 3: No words found
    board3 = [["a", "b"], ["c", "d"]]
    words3 = ["abcd"]
    result3 = solution.findWords(board3, words3)
    assert result3 == []

    # Test case 4: Empty board
    board4 = []
    words4 = ["a"]
    result4 = solution.findWords(board4, words4)
    assert result4 == []

    # Test case 5: Empty words
    board5 = [["a", "b"], ["c", "d"]]
    words5 = []
    result5 = solution.findWords(board5, words5)
    assert result5 == []

    # Test case 6: Single character words
    board6 = [["a", "b"], ["c", "d"]]
    words6 = ["a", "b", "c", "d"]
    result6 = solution.findWords(board6, words6)
    expected6 = ["a", "b", "c", "d"]
    assert sorted(result6) == sorted(expected6)

    print("All test cases passed!")


if __name__ == "__main__":
    test_word_search_ii()
