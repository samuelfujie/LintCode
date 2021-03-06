class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        
    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.dict[val] = self.dict.get(val, []) + [len(self.list)]
        self.list.append([val, len(self.dict[val]) - 1])

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict or len(self.dict[val]) == 0:
            return False
        index = self.dict[val][-1]
        new_val, dict_pos = self.list[-1]
        
        self.list[index] = [new_val, dict_pos]
        self.dict[new_val][dict_pos] = index
        
        self.dict[val].pop()
        self.list.pop()

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        if not self.list:
            return None
        return self.list[random.randrange(len(self.list))][0]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()