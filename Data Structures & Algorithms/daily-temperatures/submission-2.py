class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while st and st[-1][0] < temperatures[i]:
                val, ind = st.pop()
                res[ind] = i-ind
            st.append([temperatures[i],i])
        
        return res