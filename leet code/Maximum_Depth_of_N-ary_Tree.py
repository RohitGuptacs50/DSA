"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(root, length):
            if not root:
                return None
            
            length += 1
            
            if not root.children:
                res.append(length)
            else:
                for child in root.children:
                    dfs(child, length)
                    
        
        res = []
        dfs(root, 0)
        if not res:
            return 0
        
        return max(res)
