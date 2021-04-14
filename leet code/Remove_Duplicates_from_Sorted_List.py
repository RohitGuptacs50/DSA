# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        tmp = head
        
        while head.next != None:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return tmp
