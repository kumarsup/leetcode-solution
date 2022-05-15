'''
string = ch
shift = s[0]
hash = chr((ord(ch)-ord(string[0]))%26 + ord('a'))

xyz - abc
bcd - abc


n = len of arr
k = max len of one string in arr

TC - O(n*k)
SC - O(n*k)

'''
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def getHash(string):
            shift = ord(string[0])
            hashkey = ''
            
            for ch in string:
                val = chr((ord(ch)-shift)%26 + ord('a'))
                hashkey = hashkey+val
                
            return hashkey
        
        resultMap = defaultdict(list)
        for string in strings:
            hashKey = getHash(string)
            resultMap[hashKey].append(string)
            
        return resultMap.values()
            
        