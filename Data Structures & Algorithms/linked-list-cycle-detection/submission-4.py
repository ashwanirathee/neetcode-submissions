# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p = head
        fast_p = head
        while fast_p and fast_p.next and fast_p.next.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p.val == fast_p.val:
                return True

        return False