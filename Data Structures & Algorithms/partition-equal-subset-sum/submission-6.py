class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2: return False
        se = set()
        half = s//2
        for num in nums:
            if num == half: return True
            l = list(se)
            se_new = set()

            for item in l:
                se_new.add(item + num)
                se_new.add(item)
            se_new.add(num)
            se = se_new
            if half in se: return True
        return False