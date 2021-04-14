# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def right_rec(node, lvl):
            if node:
                if lvl > len(ans):
                    ans.append(node.val)
                right_rec(node.right, lvl + 1)
                right_rec(node.left, lvl + 1)
        right_rec(root, 1)
        
        return ans
        
