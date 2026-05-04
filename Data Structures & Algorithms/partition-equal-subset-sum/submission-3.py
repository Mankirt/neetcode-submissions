class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2: return False
        target = sum(nums)/2
        d = set()
        d.add(0)

        for num in nums:
            temp = set()
            for item in d:
                temp.add(item)
                if item + num == target: return True
                elif item + num < target:
                    temp.add(item+num)
            d = temp
        
        return False
