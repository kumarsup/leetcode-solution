'''
typei, colori, namei
ruleKey == "color" and ruleValue == colori


'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count  = 0 
        for item in items:
            if ruleKey == "type" and ruleValue == item[0] or ruleKey == "color" and ruleValue == item[1] or ruleKey == "name" and ruleValue == item[2]:
                count += 1
                
        return count