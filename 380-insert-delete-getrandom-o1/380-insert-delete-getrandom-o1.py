class RandomizedSet:

    def __init__(self):
        self.hashmap = defaultdict(int)
        self.arr = [] 
        
    def insert(self, val: int) -> bool:
        if val in self.hashmap: return False
        self.hashmap[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap: return False
        lastElement, idx = self.arr[-1], self.hashmap[val]
        self.arr[idx], self.hashmap[lastElement] = lastElement, idx
        self.arr.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        n = len(self.arr)
        rand = random.randint(0, n-1)
        return self.arr[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()