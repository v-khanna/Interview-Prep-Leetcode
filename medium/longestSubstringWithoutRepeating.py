class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_map = {}  # Store the last position of each character
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            # If we've seen this character before and it's after our current start
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            else:
                max_length = max(max_length, end - start + 1)

            char_map[char] = end

        return max_length


# Alternative solution using sliding window with set
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_set = set()
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            # If character is already in the window, shrink from start
            while char in char_set:
                char_set.remove(s[start])
                start += 1

            char_set.add(char)
            max_length = max(max_length, end - start + 1)

        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    # Test cases
    test_cases = [
        "abcabcbb",  # Expected: 3 ("abc")
        "bbbbb",  # Expected: 1 ("b")
        "pwwkew",  # Expected: 3 ("wke")
        "",  # Expected: 0
        "aab",  # Expected: 2 ("ab")
        "dvdf",  # Expected: 3 ("vdf")
    ]

    for s in test_cases:
        result1 = solution.lengthOfLongestSubstring(s)
        result2 = solution2.lengthOfLongestSubstring(s)
        print(f"'{s}' -> Length: {result1} (map method), {result2} (set method)")
