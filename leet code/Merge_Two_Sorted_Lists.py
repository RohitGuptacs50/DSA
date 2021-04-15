# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arra1 = []
        arra2 = []
        
        while l1:
            arra1.append(l1.val)
            l1 = l1.next
        
        while l2:
            arra2.append(l2.val)
            l2 = l2.next
            
        mrg = [None]*(len(arra1) + len(arra2))
        i = j = k = 0
        while i < len(arra1) and j < len(arra2):
            if arra1[i] < arra2[j]:
                mrg[k] = arra1[i]
                i += 1
                k += 1
            elif arra2[j] < arra1[i]:
                mrg[k] = arra2[j]
                j += 1
                k += 1
            elif arra1[i] == arra2[j]:
                mrg[k] = arra1[i]
                i += 1
                k += 1
        while i < len(arra1):
            mrg[k] = arra1[i]
            i += 1
            k += 1
        while j < len(arra2):
            mrg[k] = arra2[j]
            j += 1
            k += 1
        if len(mrg) == 0:
            head = l3 = ListNode()
            return head.next
        else:
            head = l3 = ListNode(mrg[0])
            for i in range(1,len(mrg)): 
                l3.next = ListNode(mrg[i])

                l3 = l3.next

            return head
