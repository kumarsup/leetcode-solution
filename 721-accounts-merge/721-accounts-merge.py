'''
["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]

[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]

hashmap - email: index
    - email - [1, 2]
    vals - [1], [2], [3], [1, 2], [4]

Union find - 

email- group- hashmap - email: group/index
if email repeated - union group/index - group in union find

components - 
email, group 
    - components[uf.find(group)] = email1, email2
    
mergedAccounts - 
    - loop on components:
        - name - accounts[group][0]
        - mergedAccounts.append()

'''
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            self.root[rootY] = rootX
            

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        unionFind = UnionFind(n)
        
        emailGroup = defaultdict(list)
        
        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    unionFind.union(i, emailGroup[email])
        
        components = defaultdict(list)
        for email, group in emailGroup.items():
            components[unionFind.find(group)].append(email)
        
        mergedAccounts = []
        for group, emails in components.items():
            name = accounts[group][0]
            mergedAccounts.append([name] + sorted(emails))
            
        return mergedAccounts
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        