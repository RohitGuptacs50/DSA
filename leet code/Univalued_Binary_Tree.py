# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root: return True
        
        stack = [root]
        
        unique_val = root.val
        
        
        while stack:
            
            curr = stack.pop()
            
             
            if curr:
                if not unique_val == curr.val: 
                    return False
                
                stack.append(curr.left)
                stack.append(curr.right)
        
        return True
