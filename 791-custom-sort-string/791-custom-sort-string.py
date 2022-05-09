class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = []
        for c in order:
            res.append(c*counter[c])
            counter[c] = 0
        for c in counter:
            res.append(c*counter[c])
        return ''.join(res)
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        # orderMap = {}
        # for i in range(len(order)): orderMap[order[i]] = i
        # sList = list(s)
        # sList.sort(key = lambda x: orderMap[x] if x in orderMap else 27)
        # return ''.join(sList)