class ListNode:
    def __initit__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

        """
        Time Complexity: O(1)
        The function performs a constant number of operations:
        - Copying the value of the next node to the current node.
        - Updating the next pointer to skip the next node.

        Space Complexity: O(1)
        The function uses a constant amount of additional space, independent of the list size.
        """
