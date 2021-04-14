class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        strs = ['b', 'a', 'l', 'o', 'n']
        counts = [0] * 5

        for i in range(5):
            counts[i] = text.count(strs[i])

        counts[2] = counts[2] // 2
        counts[3] = counts[3] // 2

        return min(counts)
