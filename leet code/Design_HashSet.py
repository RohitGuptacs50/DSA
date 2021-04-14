class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = []
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            self.hashTable.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            self.hashTable.remove(key)
        else:
            return
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hashTable
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
