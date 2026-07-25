# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        p1 = None
        curr2 = l2
        p2 = None

        new_start = ListNode()
        curr3 = new_start
        p3 = None

        carry = 0
        while curr1 and curr2:
            res = curr1.val + curr2.val + carry
            if res >= 10:
                res = res % 10
                carry = 1
            else:
                carry = 0

            curr3.val = res
            if curr2.next or curr1.next or carry: curr3.next = ListNode(carry)

            p1 = curr1
            p2 = curr2
            p3 = curr3
            curr1 = curr1.next
            curr2 = curr2.next
            curr3 = curr3.next

        if curr1:
            while curr1:
                res = curr1.val +  carry
                if res >= 10:
                    res = res % 10
                    carry = 1
                else:
                    carry = 0

                curr3.val = res
                if curr1.next or carry: curr3.next = ListNode(carry)

                p1 = curr1
                p3 = curr3
                curr1 = curr1.next
                curr3 = curr3.next


        if curr2: 
            while curr2:
                res = curr2.val +  carry
                if res >= 10:
                    res = res % 10
                    carry = 1
                else:
                    carry = 0

                curr3.val = res
                if curr2.next or carry: curr3.next = ListNode(carry)

                p2 = curr2
                p3 = curr3
                curr2 = curr2.next
                curr3 = curr3.next
        return new_start