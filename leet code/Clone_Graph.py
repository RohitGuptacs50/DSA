"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node, visited = {}):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        if node in visited:
            return visited[node]
        
        clone = Node(node.val)
        visited[node] = clone
        for i in node.neighbors:
            clone.neighbors.append(self.cloneGraph(i, visited))

        return clone
        
