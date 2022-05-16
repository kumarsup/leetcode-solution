'''
keep array and left index
when next add the val in 
'''
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [0]*size
        self.head = self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head+1)%self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = (self.head + 1)%self.size
        self.queue[self.head] = val
        return self.window_sum/min(self.size, self.count)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)