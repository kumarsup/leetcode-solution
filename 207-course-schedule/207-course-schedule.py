'''
numCourses = 2, prerequisites = [[1,0],[0,1]]
{
0:1
1:0
}
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            
        def checkCycle(node, seen, checked):
            if checked[node]: return False
            if seen[node]: return True
            
            seen[node] = True
            
            if node in graph:
                for nei in graph[node]:
                    if checkCycle(nei, seen, checked): return True
            seen[node] = False
            checked[node] = True
            return False
        
        checked, seen, res = [None]*numCourses, [None]*numCourses, False
        for cource in range(numCourses):
            if cource not in seen:
                if checkCycle(cource, seen, checked): return False
        return True
            
        
        