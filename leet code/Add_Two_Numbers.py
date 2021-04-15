# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
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
        
        arra1.reverse()
        arra2.reverse()
        
        x = int("".join(map(str, arra1)))
        y = int("".join(map(str, arra2)))
        z = x + y
        
        arra3 = [int(x) for x in str(z)] 
        arra3.reverse()
        
        head = l3 = ListNode(arra3[0])
        for i in range(1,len(arra3)): 
            l3.next = ListNode(arra3[i])
        
            l3 = l3.next
                       
        return head
