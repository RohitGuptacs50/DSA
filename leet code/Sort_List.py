# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        a1 = []
        ptr = head
        while ptr is not None:
            a1.append(ptr.val)
            ptr = ptr.next
            
        a1.sort()
        
        if len(a1) == 0:
            head = l3 = ListNode()
            return head.next
        else:
            head = l3 = ListNode(a1[0])
            for i in range(1,len(a1)): 
                l3.next = ListNode(a1[i])

                l3 = l3.next

            return head
