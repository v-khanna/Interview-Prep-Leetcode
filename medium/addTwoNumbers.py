# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values from the lists, defaulting to 0 if list is exhausted
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate sum and carry
            total = x + y + carry
            carry = total // 10

            # Create new node with the ones digit
            current.next = ListNode(total % 10)
            current = current.next

            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

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

    # Test case 1: 342 + 465 = 807
    l1 = createLinkedList([2, 4, 3])
    l2 = createLinkedList([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Result: {linkedListToArray(result)}")  # [7, 0, 8]

    # Test case 2: 9999999 + 9999 = 10009998
    l1 = createLinkedList([9, 9, 9, 9, 9, 9, 9])
    l2 = createLinkedList([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Result: {linkedListToArray(result)}")  # [8, 9, 9, 9, 0, 0, 0, 1]
