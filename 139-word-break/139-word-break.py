'''
s = "leetcode", wordDict = ["leet","code"]

Trie= leetcode

search word - o(wn*n)



'''
class TrieNode:
    def __init__(self):
        self.child = {}
        self.eow = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.eow = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                return False
            node.child[ch] = TrieNode()
            node = node.child[ch]
        return node.eow
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie, dp = Trie(), {}
        for word in wordDict: trie.insert(word) 
        
        def dfs(idx, node):
            nonlocal trie, dp
            key = (idx, id(node))
            if key in dp: return dp[key]
            if idx >= len(s): return node.eow
            if node.eow and dfs(idx, trie.root):  return True
            dp[key] = s[idx] in node.child and dfs(idx+1, node.child[s[idx]])
            return dp[key]
        
        return dfs(0, trie.root)
    