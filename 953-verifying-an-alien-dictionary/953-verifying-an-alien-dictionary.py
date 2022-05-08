class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wmap = collections.defaultdict(int)
        
        for idx in range(len(order)):
            wmap[order[idx]] = idx+1
            
        for word1, word2 in zip(words, words[1:]):
            length = min(len(word1), len(word2))
            flag = True
            
            for i in range(length):
                if wmap[word1[i]] < wmap[word2[i]]:
                    flag = False
                    break
                elif wmap[word1[i]] > wmap[word2[i]]:
                    return False
            if flag and len(word1) > len(word2):
                return False
        return True
                
                