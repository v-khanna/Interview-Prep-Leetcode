"""
Word Ladder (Hard)
https://leetcode.com/problems/word-ladder/

Problem: A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that: Every adjacent pair of words differs by a single letter, and every si for 1 <= i <= k is in wordList. Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord. If no such sequence exists, return 0.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5

Approach: BFS with bidirectional search
Time Complexity: O(n * 26 * L) where n is wordList size, L is word length
Space Complexity: O(n)
"""


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        Find shortest transformation sequence using BFS
        """
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        queue = [(beginWord, 1)]
        visited = {beginWord}

        while queue:
            word, length = queue.pop(0)

            if word == endWord:
                return length

            # Try changing each character
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i + 1 :]

                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))

        return 0

    def ladderLengthBidirectional(self, beginWord, endWord, wordList):
        """
        Bidirectional BFS for better performance
        """
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        beginSet = {beginWord}
        endSet = {endWord}
        visited = set()
        length = 1

        while beginSet and endSet:
            # Always work with smaller set
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            nextSet = set()

            for word in beginSet:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1 :]

                        if new_word in endSet:
                            return length + 1

                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            nextSet.add(new_word)

            beginSet = nextSet
            length += 1

        return 0

    def ladderLengthOptimized(self, beginWord, endWord, wordList):
        """
        Optimized version with better word generation
        """
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        queue = [(beginWord, 1)]
        visited = {beginWord}

        while queue:
            word, length = queue.pop(0)

            if word == endWord:
                return length

            # Generate all possible one-letter changes
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue

                    new_word = word[:i] + c + word[i + 1 :]

                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))

        return 0

    def ladderLengthWithPath(self, beginWord, endWord, wordList):
        """
        Version that also returns the transformation path
        """
        if endWord not in wordList:
            return 0, []

        wordSet = set(wordList)
        queue = [(beginWord, 1, [beginWord])]
        visited = {beginWord}

        while queue:
            word, length, path = queue.pop(0)

            if word == endWord:
                return length, path

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i + 1 :]

                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        new_path = path + [new_word]
                        queue.append((new_word, length + 1, new_path))

        return 0, []

    def ladderLengthDFS(self, beginWord, endWord, wordList):
        """
        DFS approach (less efficient but shows alternative)
        """
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        min_length = float("inf")

        def dfs(word, visited, length):
            nonlocal min_length

            if word == endWord:
                min_length = min(min_length, length)
                return

            if length >= min_length:
                return

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i + 1 :]

                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        dfs(new_word, visited, length + 1)
                        visited.remove(new_word)

        dfs(beginWord, {beginWord}, 1)
        return min_length if min_length != float("inf") else 0


def test_word_ladder():
    """Test cases for Word Ladder"""
    solution = Solution()

    # Test case 1: Basic case
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result1 = solution.ladderLength(beginWord1, endWord1, wordList1)
    assert result1 == 5

    result1_bd = solution.ladderLengthBidirectional(beginWord1, endWord1, wordList1)
    assert result1_bd == 5

    result1_opt = solution.ladderLengthOptimized(beginWord1, endWord1, wordList1)
    assert result1_opt == 5

    result1_path = solution.ladderLengthWithPath(beginWord1, endWord1, wordList1)
    assert result1_path[0] == 5

    result1_dfs = solution.ladderLengthDFS(beginWord1, endWord1, wordList1)
    assert result1_dfs == 5

    # Test case 2: No transformation possible
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    result2 = solution.ladderLength(beginWord2, endWord2, wordList2)
    assert result2 == 0

    # Test case 3: Same start and end word
    beginWord3 = "hit"
    endWord3 = "hit"
    wordList3 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result3 = solution.ladderLength(beginWord3, endWord3, wordList3)
    assert result3 == 1

    # Test case 4: Direct transformation
    beginWord4 = "hit"
    endWord4 = "hot"
    wordList4 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result4 = solution.ladderLength(beginWord4, endWord4, wordList4)
    assert result4 == 2

    # Test case 5: Empty word list
    beginWord5 = "hit"
    endWord5 = "cog"
    wordList5 = []
    result5 = solution.ladderLength(beginWord5, endWord5, wordList5)
    assert result5 == 0

    # Test case 6: Long transformation
    beginWord6 = "hit"
    endWord6 = "dog"
    wordList6 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result6 = solution.ladderLength(beginWord6, endWord6, wordList6)
    assert result6 == 4

    print("All test cases passed!")


if __name__ == "__main__":
    test_word_ladder()
