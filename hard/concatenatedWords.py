"""
Concatenated Words (Hard)
https://leetcode.com/problems/concatenated-words/

Problem: Given an array of strings words (without duplicates), return all the concatenated words in the given list of words. A concatenated word is defined as a string that is completely composed by at least two shorter words in the given array.

Example:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Approach: Dynamic Programming with Trie
Time Complexity: O(n * L^2) where n is number of words, L is max word length
Space Complexity: O(n * L)
"""


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        Find all concatenated words using dynamic programming
        """
        if not words:
            return []

        # Convert to set for O(1) lookup
        wordSet = set(words)
        result = []

        def canForm(word):
            """Check if word can be formed by concatenating other words"""
            if not word:
                return False

            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in wordSet:
                        dp[i] = True
                        break

            return dp[n]

        # Check each word
        for word in words:
            if len(word) == 0:
                continue

            # Temporarily remove current word from set
            wordSet.remove(word)

            if canForm(word):
                result.append(word)

            # Add word back to set
            wordSet.add(word)

        return result

    def findAllConcatenatedWordsInADictOptimized(self, words):
        """
        Optimized version with early termination
        """
        if not words:
            return []

        # Sort by length to process shorter words first
        words.sort(key=len)
        wordSet = set()
        result = []

        def canForm(word):
            """Check if word can be formed by concatenating other words"""
            if not word:
                return False

            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in wordSet:
                        dp[i] = True
                        break

            return dp[n]

        # Process words in order of increasing length
        for word in words:
            if len(word) == 0:
                continue

            if canForm(word):
                result.append(word)

            wordSet.add(word)

        return result

    def findAllConcatenatedWordsInADictTrie(self, words):
        """
        Trie-based approach
        """
        if not words:
            return []

        # Build trie
        trie = {}
        for word in words:
            if len(word) == 0:
                continue
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["#"] = True  # End marker

        result = []

        def canForm(word):
            """Check if word can be formed using trie"""
            if not word:
                return False

            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and isWord(word[j:i]):
                        dp[i] = True
                        break

            return dp[n]

        def isWord(word):
            """Check if word exists in trie"""
            node = trie
            for char in word:
                if char not in node:
                    return False
                node = node[char]
            return "#" in node

        def addToTrie(word):
            """Add word to trie"""
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["#"] = True

        def removeFromTrie(word):
            """Remove word from trie"""
            node = trie
            path = [node]
            for char in word:
                if char not in node:
                    return
                node = node[char]
                path.append(node)

            if "#" in node:
                del node["#"]

                # Clean up empty nodes
                for i in range(len(path) - 2, -1, -1):
                    if not path[i + 1]:
                        del path[i][word[i]]
                    else:
                        break

        # Check each word
        for word in words:
            if len(word) == 0:
                continue

            # Temporarily remove from trie
            removeFromTrie(word)

            if canForm(word):
                result.append(word)

            # Add back to trie
            addToTrie(word)

        return result

    def findAllConcatenatedWordsInADictDFS(self, words):
        """
        DFS approach with memoization
        """
        if not words:
            return []

        wordSet = set(words)
        memo = {}

        def canForm(word, count=0):
            """Check if word can be formed with at least 2 words"""
            if word in memo:
                return memo[word]

            if not word:
                return count >= 2

            result = False
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in wordSet:
                    if canForm(word[i:], count + 1):
                        result = True
                        break

            memo[word] = result
            return result

        result = []
        for word in words:
            if len(word) == 0:
                continue

            wordSet.remove(word)
            if canForm(word):
                result.append(word)
            wordSet.add(word)
            memo.clear()  # Clear memo for next word

        return result


def test_concatenated_words():
    """Test cases for Concatenated Words"""
    solution = Solution()

    # Test case 1: Basic case
    words1 = [
        "cat",
        "cats",
        "catsdogcats",
        "dog",
        "dogcatsdog",
        "hippopotamuses",
        "rat",
        "ratcatdogcat",
    ]
    result1 = solution.findAllConcatenatedWordsInADict(words1)
    expected1 = ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
    assert sorted(result1) == sorted(expected1)

    result1_opt = solution.findAllConcatenatedWordsInADictOptimized(words1)
    assert sorted(result1_opt) == sorted(expected1)

    result1_dfs = solution.findAllConcatenatedWordsInADictDFS(words1)
    assert sorted(result1_dfs) == sorted(expected1)

    # Test case 2: No concatenated words
    words2 = ["cat", "dog", "bird"]
    result2 = solution.findAllConcatenatedWordsInADict(words2)
    assert result2 == []

    # Test case 3: Empty list
    words3 = []
    result3 = solution.findAllConcatenatedWordsInADict(words3)
    assert result3 == []

    # Test case 4: Single word
    words4 = ["cat"]
    result4 = solution.findAllConcatenatedWordsInADict(words4)
    assert result4 == []

    # Test case 5: Simple concatenation
    words5 = ["a", "b", "ab"]
    result5 = solution.findAllConcatenatedWordsInADict(words5)
    assert result5 == ["ab"]

    # Test case 6: Multiple concatenations
    words6 = ["a", "b", "c", "abc", "abcd"]
    result6 = solution.findAllConcatenatedWordsInADict(words6)
    expected6 = ["abc", "abcd"]
    assert sorted(result6) == sorted(expected6)

    print("All test cases passed!")


if __name__ == "__main__":
    test_concatenated_words()
