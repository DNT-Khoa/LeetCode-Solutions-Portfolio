# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        carry = 0
        
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            v = total % 10
            carry = total // 10
            
            node = ListNode(v)
            curr.next = node
            curr = node
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        if carry != 0:
            curr.next = ListNode(1)
            
        return dummy.next
            
            