# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2

        r1 = []
        while c1:
            r1.append(str(c1.val))
            c1 = c1.next

        r2 = []
        while c2:
            r2.append(str(c2.val))
            c2 = c2.next

        n1 = int("".join(r1))
        n2 = int("".join(r2))
        n3 = str(n1+n2)
        print(n3)
        c3 = ListNode(-1)
        og = c3
        idx = 0
        while idx < len(n3):
            c3.next = ListNode(n3[idx])
            idx+=1
            c3 = c3.next
        return og.next