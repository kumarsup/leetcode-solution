class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wn = len(word)
        an = len(abbr)
        i, j = 0, 0
        
        while i < wn and j < an:
            num = 0
            while j < an and abbr[j].isdigit():
                num = num*10 + int(abbr[j])
                if not num: return False
                j += 1
                
            if num > 0:
                if i + num > wn: return False
                i = i + num
            else:
                if word[i] != abbr[j]: return False
                i+=1
                j+=1
        return i == wn and j == an
            