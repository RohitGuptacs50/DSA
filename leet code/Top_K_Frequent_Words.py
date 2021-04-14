class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_hash = {}
        for word in words:
            word_hash[word] = word_hash.get(word, 0) + 1
        words = sorted(word_hash.keys(), key = lambda w: (-word_hash[w], w))
        return words[:k]
