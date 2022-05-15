'''
sorted - 
i, j, k
res

'''
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        n1 = len(arr1)        
        n2 = len(arr2)
        n3 = len(arr3)
        
        i, j, k, res = 0, 0, 0, []
        
        while i < n1 and j < n2 and k < n3:
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i, j, k = i+1, j+1, k+1
            elif arr1[i] < arr2[j] or arr1[i] < arr3[k]:
                i+=1
            elif arr2[j] < arr1[i] or arr2[j] < arr3[k]:
                j+=1
            elif arr3[k] < arr1[i] or arr3[k] < arr2[j]:
                k+=1
        return res