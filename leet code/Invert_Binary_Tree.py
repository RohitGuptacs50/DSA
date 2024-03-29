# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            node=stack.pop()
            
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
                
            node.left,node.right=node.right,node.left
            
        return root
        
