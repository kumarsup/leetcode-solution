class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderMap = {}
        
        for i in range(len(order)):
            orderMap[order[i]] = i
            
        sList = list(s)
        sList.sort(key = lambda x: orderMap[x] if x in orderMap else 27)
        return ''.join(sList)