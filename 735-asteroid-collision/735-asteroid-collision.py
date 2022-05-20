class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for num in asteroids:
            while stack and num < 0 < stack[-1]:
                if stack[-1] < -num:
                    stack.pop()
                    continue
                elif stack[-1] == -num:
                    stack.pop()
                break
            else:
                stack.append(num)
        return stack
                 
                