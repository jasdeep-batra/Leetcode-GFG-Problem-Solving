class RandomizedSet:

    def __init__(self):
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.arr:
            ind = self.arr.index(val)
            self.arr.pop(ind)
            return True
        return False
        
    def getRandom(self) -> int:
        ind = random.randint(0,len(self.arr)-1)
        return self.arr[ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()