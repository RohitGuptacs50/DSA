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
            res.append(node.val)
            self.inorder(node.right, res)
            
        else:
            return
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.inorder(root, res)
        print(res)
        min = 1000
        for i in range(len(res) - 1):
            for j in range(i + 1, len(res)):
                if min > abs(res[i] - res[j]):
                    min = abs(res[i] - res[j])
                    
        return min
