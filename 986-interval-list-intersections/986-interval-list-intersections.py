'''
[0,2],[5,10],[13,23],[24,25]
[1,5],[8,12],[15,24],[25,26]


[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]
second


'''
class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        fn = len(first)
        sn = len(second)
        
        i, j, res =  0, 0, []
        
        while i < fn and j < sn:
            low = max(first[i][0], second[j][0])
            high = min(first[i][1], second[j][1])
            
            if low<=high:
                res.append([low, high])
            
            if first[i][1] < second[j][1]:
                i+=1
            else:
                j+=1
        return res