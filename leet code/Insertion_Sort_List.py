# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arra = []
        
        while head:
            arra.append(head.val)
            head = head.next
            
        for i in range(1, len(arra)):
            key = arra[i]
            
            j = i - 1
            
            while j >= 0 and key < arra[j]:
                arra[j + 1] = arra[j]
                j -= 1
            arra[j + 1] = key
            
        if len(arra) == 0:
            return head
        else:
            
            head = l3 = ListNode(arra[0])
            for i in range(1,len(arra)): 
                l3.next = ListNode(arra[i])

                l3 = l3.next

            return head
