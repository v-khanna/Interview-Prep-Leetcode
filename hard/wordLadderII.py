"""
Word Ladder II (Hard)
https://leetcode.com/problems/word-ladder-ii/

Problem: A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that: Every adjacent pair of words differs by a single letter, and every si for 1 <= i <= k is in wordList. Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

Approach: BFS with path tracking
Time Complexity: O(n * 26^l * l) where n is wordList size, l is word length
Space Complexity: O(n * l)
"""


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        Find all shortest transformation sequences using BFS
        """
        if endWord not in wordList:
            return []

        wordSet = set(wordList)
        queue = [(beginWord, [beginWord])]
        visited = {beginWord}
        result = []
        min_length = float("inf")

        while queue:
            word, path = queue.pop(0)

            if len(path) > min_length:
                break

            if word == endWord:
                if len(path) < min_length:
                    result = []
                    min_length = len(path)
                result.append(path)
                continue

            # Generate all possible one-letter changes
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue

                    new_word = word[:i] + c + word[i + 1 :]

                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, path + [new_word]))

        return result

    def findLaddersOptimized(self, beginWord, endWord, wordList):
        """
        Optimized version with bidirectional BFS
        """
        if endWord not in wordList:
            return []

        wordSet = set(wordList)

        # Bidirectional BFS to find shortest distance
        def findShortestDistance():
            beginSet = {beginWord}
            endSet = {endWord}
            visited = set()
            distance = 1

            while beginSet and endSet:
                if len(beginSet) > len(endSet):
                    beginSet, endSet = endSet, beginSet

                nextSet = set()

                for word in beginSet:
                    for i in range(len(word)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            new_word = word[:i] + c + word[i + 1 :]

                            if new_word in endSet:
                                return distance + 1

                            if new_word in wordSet and new_word not in visited:
                                visited.add(new_word)
                                nextSet.add(new_word)

                beginSet = nextSet
                distance += 1

            return 0

        shortest_distance = findShortestDistance()
        if shortest_distance == 0:
            return []

        # DFS to find all paths with shortest distance
        result = []

        def dfs(word, path, remaining_steps):
            if remaining_steps == 0:
                if word == endWord:
                    result.append(path[:])
                return

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue

                    new_word = word[:i] + c + word[i + 1 :]

                    if new_word in wordSet:
                        path.append(new_word)
                        dfs(new_word, path, remaining_steps - 1)
                        path.pop()

        dfs(beginWord, [beginWord], shortest_distance - 1)
        return result

    def findLaddersWithLevel(self, beginWord, endWord, wordList):
        """
        Level-by-level BFS approach
        """
        if endWord not in wordList:
            return []

        wordSet = set(wordList)
        level = {beginWord}
        parents = {beginWord: []}
        result = []

        while level and endWord not in parents:
            next_level = {}

            for word in level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        new_word = word[:i] + c + word[i + 1 :]

                        if new_word in wordSet and new_word not in parents:
                            if new_word not in next_level:
                                next_level[new_word] = []
                            next_level[new_word].append(word)

            level = next_level
            parents.update(next_level)

        if endWord not in parents:
            return []

        # Reconstruct paths
        def getPaths(word):
            if word == beginWord:
                return [[beginWord]]

            paths = []
            for parent in parents[word]:
                for path in getPaths(parent):
                    paths.append(path + [word])

            return paths

        return getPaths(endWord)

    def findLaddersBidirectional(self, beginWord, endWord, wordList):
        """
        Bidirectional BFS with path reconstruction
        """
        if endWord not in wordList:
            return []

        wordSet = set(wordList)

        # Build graph using BFS
        graph = {}
        queue = [beginWord]
        visited = {beginWord}
        found = False

        while queue and not found:
            level_size = len(queue)
            level = set()

            for _ in range(level_size):
                word = queue.pop(0)

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        new_word = word[:i] + c + word[i + 1 :]

                        if new_word == endWord:
                            found = True

                        if new_word in wordSet:
                            if new_word not in graph:
                                graph[new_word] = set()
                            graph[new_word].add(word)

                            if new_word not in visited:
                                visited.add(new_word)
                                level.add(new_word)

            for word in level:
                queue.append(word)

        if not found:
            return []

        # DFS to find all paths
        result = []

        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in graph.get(word, []):
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])
        return result


def test_word_ladder_ii():
    """Test cases for Word Ladder II"""
    solution = Solution()

    # Test case 1: Basic case
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result1 = solution.findLadders(beginWord1, endWord1, wordList1)
    expected1 = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"],
    ]
    assert len(result1) == len(expected1)
    assert all(path in expected1 for path in result1)

    result1_opt = solution.findLaddersOptimized(beginWord1, endWord1, wordList1)
    assert len(result1_opt) == len(expected1)

    result1_level = solution.findLaddersWithLevel(beginWord1, endWord1, wordList1)
    assert len(result1_level) == len(expected1)

    result1_bd = solution.findLaddersBidirectional(beginWord1, endWord1, wordList1)
    assert len(result1_bd) == len(expected1)

    # Test case 2: No transformation possible
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    result2 = solution.findLadders(beginWord2, endWord2, wordList2)
    assert result2 == []

    # Test case 3: Same start and end word
    beginWord3 = "hit"
    endWord3 = "hit"
    wordList3 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result3 = solution.findLadders(beginWord3, endWord3, wordList3)
    assert result3 == [["hit"]]

    # Test case 4: Direct transformation
    beginWord4 = "hit"
    endWord4 = "hot"
    wordList4 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result4 = solution.findLadders(beginWord4, endWord4, wordList4)
    assert result4 == [["hit", "hot"]]

    # Test case 5: Empty word list
    beginWord5 = "hit"
    endWord5 = "cog"
    wordList5 = []
    result5 = solution.findLadders(beginWord5, endWord5, wordList5)
    assert result5 == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_word_ladder_ii()
