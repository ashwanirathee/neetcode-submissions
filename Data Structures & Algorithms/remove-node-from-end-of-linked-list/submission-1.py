# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            l+=1
            curr = curr.next
            
        curr = head
        i = 0
        prev = None
        while curr:
            if i == l - n:
                if not prev:
                    if curr.next:
                        return curr.next
                    else:
                        return None
                else:
                    prev.next = curr.next
            i+=1
            prev = curr
            curr=curr.next

        return head