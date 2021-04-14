# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def tree_root(self, res):   
            
              
                mid = len(res) // 2

                root = TreeNode(res[mid])
                if len(res) > 1:
                    root.left = self.tree_root(res[:mid])
                    if mid + 1  < len(res):
                        root.right = self.tree_root(res[mid + 1:])
            
                return root
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
            
        root = self.tree_root(res)
        return root
