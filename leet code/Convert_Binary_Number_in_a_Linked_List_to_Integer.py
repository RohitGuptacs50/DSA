# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        
        arra = []
        
        while head:
            arra.append(head.val)
            head = head.next
            
        num = [str(i) for i in arra]
        
        res = ("".join(num))
        return int(res, 2)
