"""
Implement Trie (Prefix Tree) (Medium)
https://leetcode.com/problems/implement-trie-prefix-tree/

Problem: A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Example:
Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output: [null, null, true, false, true, null, true]

Approach: Trie data structure with nodes
Time Complexity: O(m) for insert/search/startsWith where m is word length
Space Complexity: O(ALPHABET_SIZE * m * n) where m is avg word length, n is number of words
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

    def delete(self, word):
        """
        Delete a word from the trie.
        """

        def delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            should_delete = delete_helper(node.children[char], word, index + 1)

            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end

            return False

        delete_helper(self.root, word, 0)

    def getWordsWithPrefix(self, prefix):
        """
        Get all words that start with the given prefix.
        """
        node = self.root

        # Navigate to the end of prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # Collect all words from this node
        words = []

        def collect_words(node, current_word):
            if node.is_end:
                words.append(current_word)

            for char, child in node.children.items():
                collect_words(child, current_word + char)

        collect_words(node, prefix)
        return words

    def countWordsStartingWith(self, prefix):
        """
        Count number of words that start with the given prefix.
        """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]

        count = 0

        def count_words(node):
            nonlocal count
            if node.is_end:
                count += 1

            for child in node.children.values():
                count_words(child)

        count_words(node)
        return count


class TrieOptimized:
    def __init__(self):
        """
        Optimized trie implementation
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        if not word:
            return

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        if not word:
            return False

        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


def test_trie():
    """Test cases for Trie implementation"""

    # Test basic operations
    trie = Trie()

    # Test insert and search
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True

    trie.insert("app")
    assert trie.search("app") == True

    # Test startsWith
    assert trie.startsWith("a") == True
    assert trie.startsWith("ap") == True
    assert trie.startsWith("app") == True
    assert trie.startsWith("apple") == True
    assert trie.startsWith("b") == False

    # Test empty string
    trie.insert("")
    assert trie.search("") == True
    assert trie.startsWith("") == True

    # Test delete
    trie.delete("apple")
    assert trie.search("apple") == False
    assert trie.search("app") == True

    # Test getWordsWithPrefix
    trie.insert("apple")
    trie.insert("application")
    trie.insert("apply")
    words = trie.getWordsWithPrefix("app")
    expected = ["app", "apple", "application", "apply"]
    assert sorted(words) == sorted(expected)

    # Test countWordsStartingWith
    count = trie.countWordsStartingWith("app")
    assert count == 4

    # Test optimized trie
    trie_opt = TrieOptimized()
    trie_opt.insert("test")
    assert trie_opt.search("test") == True
    assert trie_opt.search("tes") == False
    assert trie_opt.startsWith("tes") == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_trie()
