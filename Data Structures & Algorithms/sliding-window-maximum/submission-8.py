class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st = deque([]) #val, ind
        res = []
        l = 0

        for r in range(len(nums)):
            while st and st[-1][0] < nums[r]:
                st.pop()
            st.append([nums[r], r])

            if r - l + 1 >= k :
                res.append(st[0][0])
                if st[0][1] == l:
                    st.popleft()
                l += 1
        return res
