# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq
from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Use a min heap to get the smallest element from all lists
        heap = []

        # Add the first element from each list to the heap
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, list_index, node = heapq.heappop(heap)

            # Add the current node to the result
            current.next = node
            current = current.next

            # Add the next node from the same list to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, list_index, node.next))

        return dummy.next


# Alternative solution using divide and conquer
class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # Merge lists in pairs
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged = self.mergeTwoLists(lists[i], lists[i + 1])
                else:
                    merged = lists[i]
                merged_lists.append(merged)
            lists = merged_lists

        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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


# Helper function to create linked list from array
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to array
def linkedListToArray(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    # Test case 1
    lists1 = [
        createLinkedList([1, 4, 5]),
        createLinkedList([1, 3, 4]),
        createLinkedList([2, 6]),
    ]
    result1 = solution.mergeKLists(lists1)
    result1_alt = solution2.mergeKLists(lists1)
    print(
        f"Merged result: {linkedListToArray(result1)} (heap), {linkedListToArray(result1_alt)} (divide&conquer)"
    )
    # Expected: [1, 1, 2, 3, 4, 4, 5, 6]

    # Test case 2
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    result2_alt = solution2.mergeKLists(lists2)
    print(f"Empty lists result: {linkedListToArray(result2) if result2 else 'None'}")
    # Expected: None

    # Test case 3
    lists3 = [createLinkedList([])]
    result3 = solution.mergeKLists(lists3)
    result3_alt = solution2.mergeKLists(lists3)
    print(
        f"Single empty list result: {linkedListToArray(result3) if result3 else 'None'}"
    )
    # Expected: None
