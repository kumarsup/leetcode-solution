'''

'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node, visited = set()):
            if node in visited: return False
            if node == destination:
                return True
            visited.add(node)
            
            for nei in graph[node]:
                if dfs(nei, visited):
                    return True
            return False
        
        return dfs(source)
        