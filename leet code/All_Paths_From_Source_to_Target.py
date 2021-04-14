class Solution(object):
    
    def dfs(self, vertices, idx, graph, dest, lst):
        if vertices[-1] == dest:
            lst += [vertices]
        for v in graph[idx]:
            self.dfs(vertices+[v], v, graph, dest, lst)
        return lst
    
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.dfs([0], 0, graph, len(graph)-1, [])
        
