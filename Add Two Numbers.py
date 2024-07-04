class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy node to serve as the head of the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Iterate while either list still has nodes or there's a carry to process
        while l1 is not None or l2 is not None or carry != 0:
            # Extract values from the current nodes of both lists, or 0 if the list is exhausted
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # Calculate the sum and the new carry
            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            new_val = sum_val % 10

            # Create a new node with the calculated value and append it to the result list
            current.next = ListNode(new_val)
            current = current.next

            # Move to the next nodes in the input lists, if available
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # The result list is headed by dummy_head.next
        return dummy_head.next


# Complexity:
# Time Complexity: O(max(n,m))
# Space Complexity: O(max(n,m))

# m being the size of list 1 and n the size of list 2
