class RandomizedSet:
    
    def __init__(self):
        self.random_dict = {}
        self.random_list = []

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.random_dict:
            return False
        self.random_list.append(val)
        self.random_dict[val] = len(self.random_list) - 1

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.random_dict:
            return False
            
        index = self.random_dict[val]
        last_val = self.random_list[-1]
        
        self.random_list[index] = last_val
        self.random_dict[last_val] = index
        
        self.random_list.pop()
        del self.random_dict[val]

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        import random
        return self.random_list[random.randrange(len(self.random_list))]
        # write your code here


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()