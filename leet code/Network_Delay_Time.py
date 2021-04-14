class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = collections.defaultdict(list)
        for u, v, w in times:
            d[u].append((v, w))
            
        heap = [(0, K)]
        seen = set()
        while heap:
            time, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            if len(seen) == N:
                return time
            for tar, etime in d[node]:
                if tar not in seen:
                    heapq.heappush(heap, (etime + time, tar))
                    
        return -1
