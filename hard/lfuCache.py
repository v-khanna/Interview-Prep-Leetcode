"""
Design and implement a data structure for Least Frequently Used (LFU) cache.
Implement the LFUCache class:
- LFUCache(int capacity) Initializes the object with the capacity of the data structure.
- int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- void put(int key, int value) Update the value of the key if present, or inserts the key if not present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. If there is a tie, remove the least recently used.
Both operations must run in O(1) average time.
"""

from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._increase_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._increase_freq(key)
            return
        if len(self.key_to_val) >= self.capacity:
            # Remove the least frequently used key
            old_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[old_key]
            del self.key_to_freq[old_key]
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

    def _increase_freq(self, key):
        freq = self.key_to_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None


# Test cases
if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1))  # returns 1
    lfu.put(3, 3)  # evicts key 2
    print(lfu.get(2))  # returns -1 (not found)
    print(lfu.get(3))  # returns 3
    lfu.put(4, 4)  # evicts key 1
    print(lfu.get(1))  # returns -1 (not found)
    print(lfu.get(3))  # returns 3
    print(lfu.get(4))  # returns 4
