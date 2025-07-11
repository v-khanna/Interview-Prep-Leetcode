"""
Alien Dictionary (Hard)
https://leetcode.com/problems/alien-dictionary/

Problem: There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language. Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple valid orderings, return any of them.

Example:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Approach: Topological Sort with DFS/BFS
Time Complexity: O(C) where C is total number of characters
Space Complexity: O(1) since alphabet size is fixed
"""


class Solution:
    def alienOrder(self, words):
        """
        Find alien dictionary order using topological sort
        """
        if not words:
            return ""

        # Build adjacency list and in-degree count
        adj = {c: set() for word in words for c in word}
        in_degree = {c: 0 for c in adj}

        # Build graph from word comparisons
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            # Check if word2 is a prefix of word1 (invalid case)
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            # Find first different character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break

        # Topological sort using BFS
        queue = [c for c in in_degree if in_degree[c] == 0]
        result = []

        while queue:
            char = queue.pop(0)
            result.append(char)

            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if all characters were processed
        if len(result) != len(adj):
            return ""

        return "".join(result)

    def alienOrderDFS(self, words):
        """
        DFS approach with cycle detection
        """
        if not words:
            return ""

        # Build adjacency list
        adj = {c: set() for word in words for c in word}

        # Build graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
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

            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False

            rec_stack.remove(char)
            result.append(char)
            return True

        # Process all characters
        for char in adj:
            if char not in visited:
                if not dfs(char):
                    return ""

        return "".join(reversed(result))

    def alienOrderOptimized(self, words):
        """
        Optimized version with early termination
        """
        if not words:
            return ""

        # Build graph
        adj = {}
        in_degree = {}

        # Initialize all characters
        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = set()
                    in_degree[char] = 0

        # Build edges
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            # Invalid case: longer word is prefix of shorter word
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            # Find first difference
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break

        # Kahn's algorithm
        queue = [char for char in in_degree if in_degree[char] == 0]
        result = []

        while queue:
            char = queue.pop(0)
            result.append(char)

            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(result) if len(result) == len(adj) else ""

    def alienOrderUnionFind(self, words):
        """
        Union-Find approach (alternative method)
        """
        if not words:
            return ""

        # Build graph
        adj = {c: set() for word in words for c in word}

        # Build edges
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        # Topological sort with cycle detection
        visited = set()
        temp_visited = set()
        result = []

        def has_cycle(char):
            if char in temp_visited:
                return True
            if char in visited:
                return False

            temp_visited.add(char)

            for neighbor in adj[char]:
                if has_cycle(neighbor):
                    return True

            temp_visited.remove(char)
            visited.add(char)
            result.append(char)
            return False

        # Check for cycles and build result
        for char in adj:
            if char not in visited:
                if has_cycle(char):
                    return ""

        return "".join(reversed(result))


def test_alien_dictionary():
    """Test cases for Alien Dictionary"""
    solution = Solution()

    # Test case 1: Basic case
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    result1 = solution.alienOrder(words1)
    expected1 = "wertf"
    assert result1 == expected1

    result1_dfs = solution.alienOrderDFS(words1)
    assert result1_dfs == expected1

    result1_opt = solution.alienOrderOptimized(words1)
    assert result1_opt == expected1

    result1_uf = solution.alienOrderUnionFind(words1)
    assert result1_uf == expected1

    # Test case 2: Invalid case (cycle)
    words2 = ["z", "x", "z"]
    result2 = solution.alienOrder(words2)
    assert result2 == ""

    # Test case 3: Single word
    words3 = ["abc"]
    result3 = solution.alienOrder(words3)
    assert result3 == "abc"

    # Test case 4: Empty list
    words4 = []
    result4 = solution.alienOrder(words4)
    assert result4 == ""

    # Test case 5: Invalid prefix case
    words5 = ["abc", "ab"]
    result5 = solution.alienOrder(words5)
    assert result5 == ""

    # Test case 6: Multiple valid orderings
    words6 = ["a", "b", "c"]
    result6 = solution.alienOrder(words6)
    assert len(result6) == 3 and set(result6) == {"a", "b", "c"}

    print("All test cases passed!")


if __name__ == "__main__":
    test_alien_dictionary()
