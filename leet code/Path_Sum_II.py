# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(node, total, path):
            if node is not None:
                path.append(node.val)
                total = total - node.val
                if total == 0 and node.left is None and node.right is None:
                    res.append(path)
                else:
                    dfs(node.left, total, path[:])
                    dfs(node.right, total, path[:])
                    
        dfs(root, sum, [])
        return res
                        
                    
