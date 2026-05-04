class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(m):
            crr = 0
            sub = 1
            for num in nums:
                crr += num
                if crr > m:
                    sub += 1
                    crr= num
            return sub <= k
                
        
        
        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            m = l + (r-l)//2

            if check(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res