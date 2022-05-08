'''
numCourses = 2, prerequisites = [[1,0],[0,1]]
{
0:1
1:0
}
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
            
        def dfs(node, seen, checked):
            if checked[node]: return False
            if seen[node]: return True
            seen[node] = True
            for nei in graph[node]:
                 if dfs(nei, seen, checked): return True
            checked[node] = True
            seen[node] = False
            return False
    
        seen = [None]*numCourses
        checked = [None]*numCourses
        
        for cource in range(numCourses):
            if dfs(cource, seen, checked): return False
        return True
            