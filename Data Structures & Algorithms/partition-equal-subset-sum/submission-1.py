class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)/2
        ans = set()
        ans.add(0)

        for num in nums:
            temp = set()
            for t in ans:
                temp.add(t+num)
                temp.add(t)
            if target in temp:
                return True
            ans = temp
        return False