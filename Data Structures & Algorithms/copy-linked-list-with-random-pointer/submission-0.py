"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        mapd = {}
        copied = []
        i = 0
        while curr:
            mapd[curr] = i
            curr_copy = Node(curr.val)
            copied.append(curr_copy)
            curr = curr.next
            i+=1

        curr = head
        i = 0
        while curr:
            new = copied[i]
            if i+1 < len(copied):
                new.next = copied[i+1]
            if curr.random:
                new.random = copied[mapd[curr.random]]
            curr = curr.next
            i+=1
        return copied[0] if copied else None