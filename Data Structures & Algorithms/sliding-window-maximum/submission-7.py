class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        st = []
        for i,v in enumerate(nums):
            while st and st[-1][0] <= v:
                st.pop()
            st.append([v,i])
            if i>=k-1:
                while st[0][1] < i-(k-1):
                    st.pop(0)
                ans.append(st[0][0])
        
        return ans
