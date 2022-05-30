class Logger:

    def __init__(self):
        self.hashmap = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hashmap or timestamp - self.hashmap[message] >= 10:
            self.hashmap[message] = timestamp
            return True
        return False
            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)