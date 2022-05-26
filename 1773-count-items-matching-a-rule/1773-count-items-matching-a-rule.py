'''
typei, colori, namei
ruleKey == "color" and ruleValue == colori


'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count  = 0 
        valmap = {"type": 0,  "color": 1, "name": 2}
        
        for item in items:
            if ruleValue == item[valmap[ruleKey]]:
                count += 1
        return count