"""
Alien Dictionary (Hard)
https://leetcode.com/problems/alien-dictionary/

Problem: Given a sorted dictionary of an alien language, find the order of characters.

Example:
Input: ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"

Approach: Topological Sort with DFS
Time Complexity: O(V + E) where V is number of unique characters, E is number of edges
Space Complexity: O(V + E)
"""

from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words):
        """
        Find the order of characters in alien dictionary using topological sort
        """
        # Build adjacency list and in-degree count
        graph = defaultdict(set)
        in_degree = defaultdict(int)

        # Initialize all characters with 0 in-degree
        for word in words:
            for char in word:
                in_degree[char] = 0

        # Build graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            # Check if word2 is a prefix of word1 (invalid case)
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            # Find first different character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break

        # Topological sort using BFS (Kahn's algorithm)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if we have a valid topological order
        if len(result) != len(in_degree):
            return ""

        return "".join(result)

    def alienOrderDFS(self, words):
        """
        Alternative approach using DFS with cycle detection
        """
        # Build adjacency list
        graph = defaultdict(set)

        # Initialize all characters
        for word in words:
            for char in word:
                graph[char] = set()

        # Build graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        # DFS with cycle detection
        visited = set()
        rec_stack = set()
        result = []

        def dfs(char):
            if char in rec_stack:
                return False  # Cycle detected
            if char in visited:
                return True

            visited.add(char)
            rec_stack.add(char)

            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False

            rec_stack.remove(char)
            result.append(char)
            return True

        # Process all characters
        for char in list(graph.keys()):
            if char not in visited:
                if not dfs(char):
                    return ""

        return "".join(result[::-1])  # Reverse for correct order


def test_alien_dictionary():
    """Test cases for Alien Dictionary"""
    solution = Solution()

    # Test case 1: Basic case
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    assert solution.alienOrder(words1) == "wertf"
    assert solution.alienOrderDFS(words1) == "wertf"

    # Test case 2: Invalid case (cycle)
    words2 = ["z", "x", "z"]
    assert solution.alienOrder(words2) == ""
    assert solution.alienOrderDFS(words2) == ""

    # Test case 3: Single word
    words3 = ["abc"]
    assert solution.alienOrder(words3) == "abc"
    assert solution.alienOrderDFS(words3) == "abc"

    # Test case 4: Empty input
    words4 = []
    assert solution.alienOrder(words4) == ""
    assert solution.alienOrderDFS(words4) == ""

    # Test case 5: Invalid prefix case
    words5 = ["abc", "ab"]
    assert solution.alienOrder(words5) == ""
    assert solution.alienOrderDFS(words5) == ""

    print("All test cases passed!")


if __name__ == "__main__":
    test_alien_dictionary()
