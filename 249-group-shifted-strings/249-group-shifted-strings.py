class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def shiftLetter(letter, shift):
            return chr((ord(letter)-shift)%26+ord('a'))
        
        def getHash(string):
            shift = ord(string[0])
            return ''.join(shiftLetter(letter, shift) for letter in string)
        
        groups = defaultdict(list)
        
        for word in strings:
            hashKey = getHash(word)
            groups[hashKey].append(word)
        return list(groups.values())
        