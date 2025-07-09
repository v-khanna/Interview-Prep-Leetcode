"""
Given two words, beginWord and endWord, and a dictionary's word list, find all shortest transformation sequences from beginWord to endWord, such that:
- Only one letter can be changed at a time
- Each transformed word must exist in the word list
Return all shortest transformation sequences.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1 :]
                        if new_word in wordSet:
                            new_layer[new_word] += [j + [new_word] for j in layer[word]]
            wordSet -= set(new_layer.keys())
            layer = new_layer
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution.findLadders(beginWord, endWord, wordList))
    # Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
