# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = list1
        l2_curr = list2
        l3_init = ListNode()
        l3_curr = l3_init
        count = 0
        while l1_curr and l2_curr:
            print(l1_curr.val, l2_curr.val)
            if l1_curr.val <= l2_curr.val:
                l3_curr.next = l1_curr
                l1_curr = l1_curr.next
            else: 
                # if l1_curr.val > l2_curr.val:
                l3_curr.next = l2_curr
                l2_curr = l2_curr.next
            l3_curr = l3_curr.next

        if l1_curr:
            l3_curr.next = l1_curr
        if l2_curr:
            l3_curr.next = l2_curr


        return l3_init.next