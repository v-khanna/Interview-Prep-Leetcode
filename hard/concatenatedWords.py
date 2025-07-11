"""
Concatenated Words (Hard)
https://leetcode.com/problems/concatenated-words/

Problem: Given an array of strings words, return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is completely composed by at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Approach: Trie + DFS with memoization
Time Complexity: O(n * L²) where n is number of words, L is max word length
Space Complexity: O(n * L)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        Find all concatenated words using Trie and DFS
        """
        # Build trie
        trie = TrieNode()
        for word in words:
            if word:  # Skip empty strings
                self._insert(trie, word)

        result = []
        for word in words:
            if word and self._can_form(word, trie, 0, 0):
                result.append(word)

        return result

    def _insert(self, root, word):
        """Insert word into trie"""
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def _can_form(self, word, trie, start, count):
        """
        Check if word can be formed by concatenating other words
        count: number of words used so far
        """
        if start == len(word):
            return count >= 2

        node = trie
        for i in range(start, len(word)):
            char = word[i]
            if char not in node.children:
                return False

            node = node.children[char]
            if node.is_end:
                # Try to form the rest of the word
                if self._can_form(word, trie, i + 1, count + 1):
                    return True

        return False

    def findAllConcatenatedWordsInADictOptimized(self, words):
        """
        Optimized approach using set and DFS with memoization
        """
        # Convert to set for O(1) lookup
        word_set = set(words)
        memo = {}

        def can_form(word, count=0):
            if word in memo:
                return memo[word]

            if count > 0 and word in word_set:
                memo[word] = True
                return True

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in word_set and can_form(suffix, count + 1):
                    memo[word] = True
                    return True

            memo[word] = False
            return False

        result = []
        for word in words:
            if word and can_form(word):
                result.append(word)

        return result

    def findAllConcatenatedWordsInADictDP(self, words):
        """
        Dynamic programming approach
        """
        word_set = set(words)
        result = []

        for word in words:
            if not word:
                continue

            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break

            # Check if word can be formed by at least 2 other words
            if dp[n]:
                # Verify it's not just a single word
                for i in range(1, n):
                    if dp[i] and word[i:] in word_set:
                        result.append(word)
                        break

        return result

    def findAllConcatenatedWordsInADictTrieOptimized(self, words):
        """
        Optimized Trie approach with early termination
        """
        # Sort words by length to process shorter words first
        words.sort(key=len)

        trie = TrieNode()
        result = []

        for word in words:
            if not word:
                continue

            if self._can_form_optimized(word, trie):
                result.append(word)
            else:
                self._insert(trie, word)

        return result

    def _can_form_optimized(self, word, trie):
        """Optimized version that stops early"""
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            node = trie
            for j in range(i, n):
                char = word[j]
                if char not in node.children:
                    break

                node = node.children[char]
                if node.is_end:
                    dp[j + 1] = True

        return dp[n]


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

    result1_dp = solution.findAllConcatenatedWordsInADictDP(words1)
    assert sorted(result1_dp) == sorted(expected1)

    result1_trie = solution.findAllConcatenatedWordsInADictTrieOptimized(words1)
    assert sorted(result1_trie) == sorted(expected1)

    # Test case 2: Simple concatenation
    words2 = ["cat", "dog", "catdog"]
    result2 = solution.findAllConcatenatedWordsInADict(words2)
    expected2 = ["catdog"]
    assert result2 == expected2

    # Test case 3: No concatenated words
    words3 = ["cat", "dog", "bird"]
    result3 = solution.findAllConcatenatedWordsInADict(words3)
    expected3 = []
    assert result3 == expected3

    # Test case 4: Empty words
    words4 = ["", "cat", "dog", "catdog"]
    result4 = solution.findAllConcatenatedWordsInADict(words4)
    expected4 = ["catdog"]
    assert result4 == expected4

    # Test case 5: Single word
    words5 = ["cat"]
    result5 = solution.findAllConcatenatedWordsInADict(words5)
    expected5 = []
    assert result5 == expected5

    # Test case 6: Empty input
    words6 = []
    result6 = solution.findAllConcatenatedWordsInADict(words6)
    expected6 = []
    assert result6 == expected6

    print("All test cases passed!")


if __name__ == "__main__":
    test_concatenated_words()
