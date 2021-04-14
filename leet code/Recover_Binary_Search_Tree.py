# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, node, res):
        if node:
            self.inorder(node.left, res)
            res.append((node.val, node))
            self.inorder(node.right, res)
        else:
            return 
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        res = []
        self.inorder(root, res)
        res1 = sorted(res)
        
        for i in range(len(res)):
            fnode = res[i][1]
            snode = res1[i][1]
            if fnode != snode:
                fnode.val, snode.val = snode.val, fnode.val
                break
        
