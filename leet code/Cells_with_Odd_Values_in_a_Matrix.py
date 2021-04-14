class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [ [0] * m for i in range(n) ]
        result = 0
        for e in indices:
            for i in range(m):
                matrix[e[0]][i] += 1
            for j in range(n):
                matrix[j][e[1]] += 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] %2 != 0:
                    result +=1
        return(result)
        
