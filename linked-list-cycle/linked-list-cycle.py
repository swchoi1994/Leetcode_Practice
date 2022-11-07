# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        r1 = r2 = head
        
        while r1 and r2:
            r1 = r1.next
            if r2.next is None:
                return False
            r2 = r2.next.next
            if r1 == r2: 
                return True
            
        return False