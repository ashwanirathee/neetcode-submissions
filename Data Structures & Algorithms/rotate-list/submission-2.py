# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        n = 0
        while curr:
            n+=1
            curr = curr.next
        print(n)
        k = k % n
        if k == 0:
            return head
        k = n-k
        print(k)

        curr = head
        while curr.next and k > 1:
            curr = curr.next
            k -=1
        print("curr_val:", curr.val)
        next_store = curr.next
        curr.next = None
        
        curr_test = next_store
        while curr_test.next:
            curr_test = curr_test.next
        
        curr_test.next = head
        return next_store