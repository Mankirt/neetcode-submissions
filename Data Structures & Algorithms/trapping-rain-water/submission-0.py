class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        m_left=height[0]
        m_right=height[-1]
        res=0
        while l<r:
            if m_left<m_right:
                l+=1
                m_left = max(m_left,height[l])
                res+= m_left - height[l]
            else:
                r-=1
                m_right = max(m_right,height[r])
                res+= m_right - height[r]
        return res