# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,node, total):
            res = 0
            total = total * 10 + node.val
            
            if not node.left and not node.right:
                self.res1 += total
                 
                
                
            for n in [node.left, node.right]:
                if n:
                    self.dfs(n, total)
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.res1 = 0      
        self.dfs(root, 0)
        return self.res1
