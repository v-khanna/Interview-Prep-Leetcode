"""
Insert Delete GetRandom O(1) (Hard)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Problem: Implement the RandomizedSet class with insert, remove, and getRandom operations, each in average O(1) time complexity.

Example:
Input: ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output: [null, true, false, true, 2, true, false, 2]

Approach: Hash Map + Array for O(1) operations
Time Complexity: O(1) average for all operations
Space Complexity: O(n)
"""

import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []  # Array to store values
        self.val_to_index = {}  # Hash map: value -> index in array

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_index:
            return False

        # Add to array and store index
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_to_index:
            return False

        # Get index of value to remove
        index = self.val_to_index[val]
        last_val = self.nums[-1]

        # Move last element to the position of element to delete
        self.nums[index] = last_val
        self.val_to_index[last_val] = index

        # Remove last element
        self.nums.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)


class RandomizedSetOptimized:
    def __init__(self):
        """
        Optimized version with better error handling
        """
        self.nums = []
        self.val_to_index = {}

    def insert(self, val):
        """
        Inserts a value to the set.
        """
        if val in self.val_to_index:
            return False

        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set.
        """
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]
        last_val = self.nums[-1]

        # Swap with last element
        self.nums[index] = last_val
        self.val_to_index[last_val] = index

        # Remove last element
        self.nums.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        if not self.nums:
            raise ValueError("Set is empty")
        return random.choice(self.nums)


class RandomizedSetWithDuplicates:
    def __init__(self):
        """
        Version that can handle duplicates (stores count)
        """
        self.nums = []
        self.val_to_indices = {}  # value -> set of indices
        self.index_to_val = {}  # index -> value

    def insert(self, val):
        """
        Inserts a value to the set.
        """
        if val not in self.val_to_indices:
            self.val_to_indices[val] = set()

        # Add to array and store index
        index = len(self.nums)
        self.nums.append(val)
        self.val_to_indices[val].add(index)
        self.index_to_val[index] = val
        return True

    def remove(self, val):
        """
        Removes a value from the set.
        """
        if val not in self.val_to_indices or not self.val_to_indices[val]:
            return False

        # Get any index of the value
        index = next(iter(self.val_to_indices[val]))
        last_index = len(self.nums) - 1
        last_val = self.nums[last_index]

        # Swap with last element
        self.nums[index] = last_val
        self.index_to_val[index] = last_val

        # Update indices
        self.val_to_indices[val].remove(index)
        self.val_to_indices[last_val].remove(last_index)
        self.val_to_indices[last_val].add(index)

        # Remove last element
        self.nums.pop()
        del self.index_to_val[last_index]

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        if not self.nums:
            raise ValueError("Set is empty")
        return random.choice(self.nums)


def test_randomized_set():
    """Test cases for Insert Delete GetRandom O(1)"""

    # Test case 1: Basic operations
    randomizedSet1 = RandomizedSet()
    assert randomizedSet1.insert(1) == True
    assert randomizedSet1.remove(2) == False
    assert randomizedSet1.insert(2) == True
    assert randomizedSet1.getRandom() in [1, 2]
    assert randomizedSet1.remove(1) == True
    assert randomizedSet1.insert(2) == False
    assert randomizedSet1.getRandom() == 2

    # Test optimized version
    randomizedSet2 = RandomizedSetOptimized()
    assert randomizedSet2.insert(1) == True
    assert randomizedSet2.remove(2) == False
    assert randomizedSet2.insert(2) == True
    assert randomizedSet2.getRandom() in [1, 2]

    # Test case 2: Empty set
    randomizedSet3 = RandomizedSet()
    assert randomizedSet3.insert(1) == True
    assert randomizedSet3.remove(1) == True
    assert randomizedSet3.insert(1) == True

    # Test case 3: Multiple insertions and removals
    randomizedSet4 = RandomizedSet()
    assert randomizedSet4.insert(1) == True
    assert randomizedSet4.insert(2) == True
    assert randomizedSet4.insert(3) == True
    assert randomizedSet4.remove(2) == True
    assert randomizedSet4.getRandom() in [1, 3]

    # Test case 4: Duplicate insertions
    randomizedSet5 = RandomizedSet()
    assert randomizedSet5.insert(1) == True
    assert randomizedSet5.insert(1) == False
    assert randomizedSet5.remove(1) == True
    assert randomizedSet5.remove(1) == False

    print("All test cases passed!")


if __name__ == "__main__":
    test_randomized_set()
