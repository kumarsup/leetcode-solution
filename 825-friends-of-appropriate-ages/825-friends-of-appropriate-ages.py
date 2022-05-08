class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        counter = Counter(ages)
        
        def canBeFriend(x, y):
            if y <= 0.5 * x + 7: return False
            if y > x: return False
            return True
        
        for a, countA in counter.items():
            for b, countB in counter.items():
                if canBeFriend(a, b):
                    count += countA*countB
                    if a == b: count -= countA
        return count