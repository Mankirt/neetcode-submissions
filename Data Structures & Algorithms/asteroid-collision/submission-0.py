class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a<0 and stack:
                while stack and stack[-1]>0 and a<0:
                    b = stack.pop()
                    if abs(b)>abs(a):
                        a = b
                    elif abs(b)==abs(a):
                        a = 0
            if a!=0:
                stack.append(a)
        return stack
