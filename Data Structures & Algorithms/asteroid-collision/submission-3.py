class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            if ast < 0 :
                while st and st[-1] > 0 and abs(st[-1])< abs(ast):
                    x = st.pop()
                if st and st[-1] > 0:
                    if abs(st[-1])==abs(ast):
                        st.pop()
                    continue
            st.append(ast)
        return st 