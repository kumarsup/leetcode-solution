class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        n = len(nums1)
        m = len(nums2)
        
        for i in range(m):
            for j in range(i+1, m):
                if nums2[j] > nums2[i]:
                    hashmap[nums2[i]] = nums2[j]
                    break
                    
        res = [-1]*n
        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                res[i] = hashmap[nums1[i]]
        return res
            