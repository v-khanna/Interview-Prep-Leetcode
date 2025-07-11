"""
Merge k Sorted Lists (Hard)
https://leetcode.com/problems/merge-k-sorted-lists/

Problem: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Approach: Priority Queue (Min Heap)
Time Complexity: O(n log k)
Space Complexity: O(k)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        """
        Merge k sorted lists using priority queue
        """
        if not lists:
            return None

        import heapq

        # Create min heap with (value, list_index, node)
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

    def mergeKListsDivideAndConquer(self, lists):
        """
        Merge k sorted lists using divide and conquer
        """
        if not lists:
            return None

        def mergeTwoLists(l1, l2):
            """Merge two sorted lists"""
            dummy = ListNode(0)
            current = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            current.next = l1 if l1 else l2
            return dummy.next

        def mergeKListsHelper(lists, start, end):
            """Recursively merge lists"""
            if start == end:
                return lists[start]
            if start > end:
                return None

            mid = (start + end) // 2
            left = mergeKListsHelper(lists, start, mid)
            right = mergeKListsHelper(lists, mid + 1, end)

            return mergeTwoLists(left, right)

        return mergeKListsHelper(lists, 0, len(lists) - 1)

    def mergeKListsIterative(self, lists):
        """
        Iterative merge approach
        """
        if not lists:
            return None

        def mergeTwoLists(l1, l2):
            """Merge two sorted lists"""
            dummy = ListNode(0)
            current = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            current.next = l1 if l1 else l2
            return dummy.next

        # Merge lists iteratively
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged = mergeTwoLists(lists[i], lists[i + 1])
                    merged_lists.append(merged)
                else:
                    merged_lists.append(lists[i])
            lists = merged_lists

        return lists[0] if lists else None

    def mergeKListsBruteForce(self, lists):
        """
        Brute force approach - collect all values and sort
        """
        if not lists:
            return None

        # Collect all values
        values = []
        for head in lists:
            current = head
            while current:
                values.append(current.val)
                current = current.next

        # Sort values
        values.sort()

        # Create new linked list
        if not values:
            return None

        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next

    def mergeKListsOptimized(self, lists):
        """
        Optimized version with early termination
        """
        if not lists:
            return None

        import heapq

        # Filter out empty lists
        valid_lists = [(i, head) for i, head in enumerate(lists) if head]

        if not valid_lists:
            return None

        # Create min heap
        heap = []
        for i, head in valid_lists:
            heapq.heappush(heap, (head.val, i, head))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


def createLinkedList(values):
    """Helper function to create linked list from values"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linkedListToValues(head):
    """Helper function to convert linked list to values"""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def test_merge_k_sorted_lists():
    """Test cases for Merge k Sorted Lists"""
    solution = Solution()

    # Test case 1: Basic case
    lists1 = [
        createLinkedList([1, 4, 5]),
        createLinkedList([1, 3, 4]),
        createLinkedList([2, 6]),
    ]
    result1 = solution.mergeKLists(lists1)
    expected1 = [1, 1, 2, 3, 4, 4, 5, 6]
    assert linkedListToValues(result1) == expected1

    result1_dc = solution.mergeKListsDivideAndConquer(lists1)
    assert linkedListToValues(result1_dc) == expected1

    result1_iter = solution.mergeKListsIterative(lists1)
    assert linkedListToValues(result1_iter) == expected1

    result1_bf = solution.mergeKListsBruteForce(lists1)
    assert linkedListToValues(result1_bf) == expected1

    result1_opt = solution.mergeKListsOptimized(lists1)
    assert linkedListToValues(result1_opt) == expected1

    # Test case 2: Empty lists
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    assert result2 is None

    # Test case 3: Single list
    lists3 = [createLinkedList([1, 2, 3])]
    result3 = solution.mergeKLists(lists3)
    expected3 = [1, 2, 3]
    assert linkedListToValues(result3) == expected3

    # Test case 4: Lists with empty lists
    lists4 = [createLinkedList([1, 2]), None, createLinkedList([3, 4])]
    result4 = solution.mergeKLists(lists4)
    expected4 = [1, 2, 3, 4]
    assert linkedListToValues(result4) == expected4

    # Test case 5: All empty lists
    lists5 = [None, None, None]
    result5 = solution.mergeKLists(lists5)
    assert result5 is None

    # Test case 6: Large lists
    lists6 = [
        createLinkedList([1, 3, 5, 7]),
        createLinkedList([2, 4, 6, 8]),
        createLinkedList([0, 9, 10]),
    ]
    result6 = solution.mergeKLists(lists6)
    expected6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert linkedListToValues(result6) == expected6

    print("All test cases passed!")


if __name__ == "__main__":
    test_merge_k_sorted_lists()
