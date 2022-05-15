class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        hashmap = defaultdict(list)
        
        for piece in pieces:
            for num in piece:
                hashmap[piece[0]].append(num)
        i = 0     
        while i < n:
            if arr[i] not in hashmap: 
                return False
            for p in hashmap[arr[i]]:
                if p != arr[i]: return False
                i+=1
        return True